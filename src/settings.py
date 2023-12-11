import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_TEST_NAME = os.getenv("DB_TEST_NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
