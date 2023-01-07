import os

class Config:
    SECRET_KEY = '820a5e8219c10a4cb40d33145ebc2639'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = 'j@gmail.com'
    MAIL_PASSWORD = 'Jon1'