import os

from sqlalchemy.engine import URL

from dotenv import load_dotenv

load_dotenv()


PUBLIC_API_URL = 'https://jservice.io/api/random?count={}'

DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_NAME')


db_url = URL.create(
        'postgresql+asyncpg',
        username=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )