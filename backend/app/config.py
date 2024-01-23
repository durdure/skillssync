from os import getenv
import secrets

MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PWD = getenv('MYSQL_PWD')
MYSQL_HOST  = getenv('MYSQL_HOST')
DB_NAME = "skillssync"

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/{}".format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, DB_NAME)
    SECRET_KEY = secrets.token_hex(16)