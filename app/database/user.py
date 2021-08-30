from app.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Date, Float
import datetime

class User(Base):
    __tablename__ = "users"

    first_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    cell_number = Column(String(12), nullable=True)
    email = Column(String(100), primary_key=True)
    password = Column(String(20), nullable=False)
    last_updated = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
