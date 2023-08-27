from sqlalchemy.orm import sessionmaker
from .models import Base
from sqlalchemy import create_engine
import os

engine = create_engine("sqlite:///db.sqlite3")

class Database:
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
            # queryset = queryset.all()
            return queryset.all()
            # if len(queryset) > 1:
            #     return queryset
            # elif len(queryset) == 1:
            #     return queryset[0]
    
    @classmethod
    def delete(cls, object):
        with cls.session(autoflush=False, bind=engine) as db:
            db.delete(object)
            db.commit()