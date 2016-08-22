import argparse
import glob
import json
import logging
import sys
import os
from collections import namedtuple
ProcessedImage = namedtuple('ProcessedImage', 'name, path, width, height, aws_url')
from PIL import Image

import tinys3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--aws-access-key-id', required=True, type=str, help='Aws access key id')
    parser.add_argument('-s', '--aws-secret-access-key-id', required=True, type=str, help='Aws secret access key')
    parser.add_argument('-f', '--folder', required=True, type=str,
                        help='the folder to make a bucket and turn into a gallery')
    parser.add_argument('-o', '--out-folder', required=True, type=str,
                        help='the folder to output the gallery to locally')
    parser.add_argument('-b', '--bucket-name', required=True, type=str,
                        help='the bucket to create and upload to aws')
    parser.add_argument('-a', '--aws-host', required=True, type=str,
                        help='aws host to prepend to the bucket')

    #
    # Destination folder for JSON will create new folder
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    #
    args = parser.parse_args()
    return vars(args)   # TODO there is a better way to do this


def upload_file(conn, bucket_name, file_name, file_path):
    if os.path.isfile(file_path):
        logger.info('Attempting to upload {} to {} bucket'.format(file_path, bucket_name))
        conn.upload(file_name, open(file_path, 'rb'), bucket_name, public=True)
    else:
        logger.error('Skpping file: {} '.format(file_path))


def get_s3_connection(aws_access_key_id, aws_secret_access_key):
    # TODO convert to connection pool
    return tinys3.Connection(aws_access_key_id, aws_secret_access_key, tls=True)


def get_local_folder_image_generator(folder):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    search_directory = os.path.join(dir_path, folder)

    if not os.path.exists(search_directory):
        raise Exception('Source: {} folder for gallery does not exist'.format(search_directory))

    print('Searching {} for JPGs'.format(search_directory))
    jpegs = glob.glob('{}/*.jpg'.format(search_directory)) # TODO regex for PNG and JPEG, TODO generator with iglob
    print('Found {} images to process'.format(len(jpegs)))

    return jpegs


def convert_to_image_thumbs(local_image_generator, out_path):
    # TODO - autdetection of the aspect ratio, it scales automatically currently, but with a real camera the targets may be different
    thumbnail_sizes= [(3200,2400),(1600,1200),(1280,960),(800,600),(640,480),(400,300),(320,240),(256,192)] # Tragetting 4:3
    #
    gallery_blocks = []
    #
    # TODO with generators
    for image_path in local_image_generator:
        temp_list = []
        for thumb_size in thumbnail_sizes:
            temp_list.append(create_image_thumb(image_path, out_path, thumb_size))
        gallery_blocks.append(temp_list)
    return gallery_blocks

def create_image_thumb(infile, outpath, size):
    try:
        # TODO some regex to check if we already processed this image. If we are perhabs updating a gallery
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        org_file_name = os.path.split(infile)[1]
        org_file_name_no_ext = os.path.splitext(org_file_name)[0]
        out_file_name = '{}-{}x{}.jpg'.format(org_file_name_no_ext, *im.size)
        out_file_full_path = os.path.join(outpath, out_file_name)
        logger.info('Image Outfile: {}'.format(out_file_full_path))
        if not os.path.exists(out_file_full_path):
            im.save(out_file_full_path, 'JPEG')
    except Exception as ex:
        logger.error('cannot create thumbnail for {}. Exception {}'.format(infile, ex))

    return ProcessedImage(name=out_file_name, path=out_file_full_path, width=im.size[0], height=im.size[1], aws_url=None)


def create_image_dict(image_set):
    # {
    #     src: 'http://example.com/example/img1_small.jpg',
    #     width: 681,
    #     height: 1024,
    #     aspectRatio: 1.5,
    #     lightboxImage: {
    #         src: 'http://example.com/example/img1_large.jpg',
    #         srcset: [
    #             'http://example.com/example/img1_1024.jpg 1024w',
    #             'http://example.com/example/img1_800.jpg 800w',
    #             'http://example.com/example/img1_500.jpg 500w',
    #             'http://example.com/example/img1_320.jpg 320w',
    #         ]
    #     }
    # }
    smallIndexer = 4
    largerIndexer = 6
    srcset=[]
    for image in image_set:
        srcset.append('{} {}w'.format(image.aws_url, image.width))

    json_to_return = {
        'src': image_set[smallIndexer].aws_url,
        'width': image_set[smallIndexer].width,
        'height': image_set[smallIndexer].height,
        'aspectRatio': float(image_set[smallIndexer].width)/image_set[smallIndexer].height,
        'lightboxImage' :{
            'src': image_set[largerIndexer].aws_url,
            'srcset': srcset
        }
    }
    return json_to_return # TODO - bad name


def main():
    args = parse_args()
    logger.info(args)
    aws_access_key_id = args['aws_access_key_id']
    aws_secret_access_key = args['aws_secret_access_key_id']
    folder = args['folder']
    out_folder = args['out_folder']
    bucket_name = args['bucket_name']
    aws_host = args['aws_host']

    if not os.path.exists(out_folder):
        raise Exception('Out folder: {} does not exists'.format(out_folder))

    out_bucket_folder = os.path.join(out_folder, bucket_name)
    if not os.path.exists(out_bucket_folder):
        logger.debug('Making bucket folder: {}'.format(out_bucket_folder))
        os.mkdir(out_bucket_folder)


    # Check that local folder exists
    # Check that there are image files in local folder
    # Create generator object to load the images (png/jpeg/jpg)
    local_image_generator = get_local_folder_image_generator(folder)

    # Create thumbnails of the images /w filename that represent the resolution and create a copy of the original with its correct resolution in name
    # Return another generator of objects with the respected image filename. We will use this to generate a json file.
    converted_images_generator = convert_to_image_thumbs(local_image_generator=local_image_generator,
                                                         out_path=out_bucket_folder)

    # Check if bucket name exists already in S3
    # Create bucket that is the same as the folder name
    s3_conn = get_s3_connection(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    bucket_name = '{}-{}'.format(aws_access_key_id.lower(),folder.lower())

    # For each file see if it is already uploaded first and upload it to the bucket if it isnt.
    # TODO - Leverage the connection pool instead of sequential
    final_dict = []
    for image_set in converted_images_generator:
        final_image_set = [] # yuck
        for image in image_set:
            upload_file(s3_conn, bucket_name, image.name, image.path)
            aws_url = '{}/{}/{}'.format(aws_host, bucket_name, image.name)
            print(aws_url)
            final_image_set.append(ProcessedImage(name=image.name, height=image.height, width=image.width, path=image.path, aws_url=aws_url))

        sorted(final_image_set, key=lambda x: x.width)    # Just for the sake of getting them in order. TODO - better way
        final_dict.append(create_image_dict(final_image_set))

    # Create json file and save it to the destination project folder.
    print(json.dumps(final_dict))
if __name__ == '__main__':
    main()