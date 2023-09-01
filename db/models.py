from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import String, Column, Integer, Boolean, Table, ForeignKey

class Base(DeclarativeBase):
    pass

# subscribtions_table = Table(
#     "subscribtions",
#     Column("user_id", Integer, ForeignKey("user.id")),
#     Column("spam_id", Integer, ForeignKey("spam.id"))
#     )


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

class Subscribtions(Base):
    __tablename__ = "subscribtions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    spam_id = Column(Integer, ForeignKey("spams.id", ondelete="CASCADE"))
