from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

with open("/home/scsm_erp/app/database/credential.json") as file:
    credential = json.load(file)

SQLALCHEMY_DATABASE_URL_DATA = f"mysql+pymysql://{credential['mysql']['user']}:{credential['mysql']['password']}@{credential['mysql']['host']}:{credential['mysql']['port']}/{credential['mysql']['database']}"

data_engine = create_engine(SQLALCHEMY_DATABASE_URL_DATA)

data_session_local = sessionmaker(autocommit=False, autoflush=False, bind=data_engine)

data_base = declarative_base()


def get_db():
    db = data_session_local()
    try:
        yield db
    finally:
        db.close()
