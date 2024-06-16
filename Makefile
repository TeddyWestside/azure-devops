hello:
	"this will be displayed at the start"
install:
	pip install --upgrade pip &&\
            pip install -r requirements.txt
test:
	python -m pytest -vv hello_test.py