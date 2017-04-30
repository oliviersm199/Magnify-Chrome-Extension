import mongo_database_client as client
import gridfs

fs = gridfs.GridFS(client.db)

class WebPageStore:
    def put(content,filename):
        result = fs.put(content,filename=filename)
        return result

    def get(file_id):
        result = fs.get(file_id)
        return result
