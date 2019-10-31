FROM python:3

ADD src /src

CMD [ "python", "./src/unit_test_calculator.py" ]
