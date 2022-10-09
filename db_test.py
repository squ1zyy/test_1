from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False)
    age = Column(Integer, nullable=False, default=1)

engine = create_engine('sqlite:///weather.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)
usr_1 = User(
    name = 'Hleb',
    age = '17'
)
usr_2 = User(
    name = 'Ann',
    age = '17'
)
session.add(usr_1)
session.add(usr_2)
session.commit()