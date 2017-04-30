import mongo_database_client as client

class User:
    '''
    A singleton object which implements a CRUD interface for users to
    work with mongodb at a higher level.
    '''
    def create_user(user):
        users = client.db.users
        user_id = client.db.users.insert_one(user)
        return user_id

    def get_user(user_id):
        user = client.db.users.find_one({"user_id":user_id})
        return user

    def replace_user(user_id,new_user):
        result = client.db.users.replace_one({"user_id":user_id},new_user)
        return result

    def delete_user(user_id):
        result = client.db.users.delete_one({"user_id":user_id})
        return result
