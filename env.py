import os

from dotenv import load_dotenv

load_dotenv()

HOME_EMAIL = os.environ['HOME_EMAIL']
PASSWORD = os.environ['PASSWORD']
RESERVE_EMAIL = os.environ['RESERVE_EMAIL']
DEBUG = bool(os.environ.get('DEBUG'))
