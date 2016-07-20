all:
	echo "all"

freeze:
	pip freeze > requirements.txt

env:

	virtualenv -p /usr/bin/python3.5 venv

s:
	bash -c "source venv/bin/activate"

run:
	honcho start


