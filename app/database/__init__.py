from sqlalchemy  import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector, pymysql

Base = declarative_base()

from app.database.user import User

engine = create_engine("mysql+pymysql://root:@127.0.0.1/login", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

connection = engine.connect()
