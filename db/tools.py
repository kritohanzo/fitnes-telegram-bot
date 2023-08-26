from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import String, Column, Integer, create_engine
import os

engine = create_engine("sqlite:///db.sqlite3")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    telegram_id = Column(Integer)

class Tools:
    session = sessionmaker(autoflush=False, bind=engine)

    @classmethod
    def check_exists_db(cls):
        if not os.path.exists('db.sqlite3'):
            Base.metadata.create_all(bind=engine)

    @classmethod
    def create(cls, object: Base):
        with cls.session(autoflush=False, bind=engine) as db:
            db.add(object)
            db.commit()

    @classmethod
    def get(cls, model, **kwargs):
        with cls.session(autoflush=False, bind=engine) as db:
            queryset = db.query(model)
            for key, value in kwargs.items():
                queryset = queryset.filter(getattr(model, key) == value)
            return queryset.all()