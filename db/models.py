from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Column, Integer, Boolean

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    telegram_id = Column(Integer)
    is_admin = Column(Boolean, default=False)

class Spam(Base):
    __tablename__ = "spams"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    picture_telegram_id = Column(String)