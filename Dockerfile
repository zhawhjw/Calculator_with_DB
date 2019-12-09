FROM python:3.7
ADD . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "./database-sql/sql-database.py"]
