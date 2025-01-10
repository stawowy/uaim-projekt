import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@0.0.0.0:5432/zoologiczny')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ACCESS_TOKEN_EXPIRATION_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRATION_MINUTES', 15)