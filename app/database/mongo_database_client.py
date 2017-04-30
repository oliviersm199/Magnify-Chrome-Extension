from pymongo import MongoClient
from settings import DATABASE_URL, DATABASE_PORT

client = MongoClient(DATABASE_URL,DATABASE_PORT)
db = client.test_database
