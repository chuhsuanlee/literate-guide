from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import config

db_engine = create_engine(config.SQLALCHEMY_DB_URI)
Session = sessionmaker(bind=db_engine)
session = Session()
