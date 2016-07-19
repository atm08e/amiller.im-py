all:
    echo "all"

dependencies:
    pip freeze > requirements.txt

run:
    honcho start

