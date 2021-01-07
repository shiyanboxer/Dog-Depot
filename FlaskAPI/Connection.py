import pymongo

def connect_db():
    """
    Connects Mongo DB cluster database so it can be accessed by APIS
    :return: if there is an error, return an error message and isError True and  if no error, return "images" (our MongoDB collection)
    """
    # https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
    # https://pymongo.readthedocs.io/en/stable/tutorial.html

    try:
        # Mmking a connection with MongoClient¶
        client = pymongo.MongoClient("mongodb+srv://shiyanboxer:NewPass@cluster0.qd7ht.mongodb.net/test")
        # get instance of the database
        db = client["ImageRepository"]
        # getting a collection (group of documents stored in MongoDB)
        images = db["images"]
    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    return images
