from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:pass@localhost:54320/mydb")
Session = sessionmaker(bind=engine)

session = Session()
