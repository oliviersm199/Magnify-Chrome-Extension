from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)

db = client.test_database

def store_user(user_id):
    users = db.users
    user = {"user_id":user_id}
    user_insert = users.insert_one(user).inserted_id
    return user_insert

print(store_user("1234"))
print(db.collection_names(include_system_collections=False))
