import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecommerce')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'ecommerce_test')