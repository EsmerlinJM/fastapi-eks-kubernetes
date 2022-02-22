import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'development')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'development')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'development')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'development')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'development')