def routes(api_handler):
    # TODO generator
    return [
        ('GET', '/', api_handler.index),
        ('GET', '/snowboarding', api_handler.snowboarding)
    ]

