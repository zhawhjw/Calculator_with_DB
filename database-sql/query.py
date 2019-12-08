from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, relationship

engine = create_engine("postgresql://postgres:pass@localhost:54320/mydb")
Session = sessionmaker(bind=engine)

session = Session()

