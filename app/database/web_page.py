import mongo_database_client as client
import gridfs

fs = gridfs.GridFS(client.db)

def put(content, filename):
    result = fs.put(content, filename=filename,encoding="utf8")
    return result

def get(file_id):
    result = fs.get(file_id)
    return result
