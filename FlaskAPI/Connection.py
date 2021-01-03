import pymongo

def connect_db():
    try:
        # Connect MongoDB cluster database. Object of cluster
        client = pymongo.MongoClient("mongodb+srv://shiyanboxer:NewPass@cluster0.qd7ht.mongodb.net/test")
        # Returns database

        DB = client["ImageRepository"]
        # Access collection - object pointing to collection

        images = DB["images"]
        # https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
    except Exception as e:
        return {"isError" : True, "errorMessage" : "An Exception has occured"}

    return images


