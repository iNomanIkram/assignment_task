from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:SECRET@db:3306/task')
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()