from os import getenv
import secrets

class Config:
    MYSQL_USER = getenv('MYSQL_USER')
    MYSQL_PWD = getenv('MYSQL_PWD')
    MYSQL_HOST = getenv('MYSQL_HOST')
    DB_NAME = "skillssync"
    SECRET_KEY = secrets.token_hex(16)
    SECURITY_PASSWORD_SALT = secrets.token_hex(16)

    # database connection
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/{}".format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, DB_NAME)

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = getenv('APP_MAIL_USERNAME') # set to alexapptest123@gmail.com
    MAIL_PASSWORD = getenv('APP_MAIL_PASSWORD') # set to ediwrygacgkgobic

    # mail accounts
    MAIL_DEFAULT_SENDER = 'alexapptest123@gmail.com'
