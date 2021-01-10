import pymongo
import env as env
# https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
# https://pymongo.readthedocs.io/en/stable/tutorial.html



def connect_db():
    """
    Connects Mongo DB database "image" collection so it can be accessed by our APIS
    :return: If there is an error, return an error message and set isError True and  if no error, return "collection" (our MongoDB collection)
    """
    try:
        # MongoDB route where collection is stored
        route = "mongodb+srv://shiyanboxer:" + env.MongoPass + "@cluster0.qd7ht.mongodb.net/test"

        # Make a Connection with MongoClient. Create a MongoClient to the running mongod instance.
        client = pymongo.MongoClient(route)

        # Get a single instance of MongoDB database (name of client)
        db = client["ImageRepository"]

        # Get a collection (group of documents stored in MongoDB, our MonogDB collection is called "images")
        collection = db["images"]

    # If connecting to the database fails, then return an error message and set isError = True
    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    # If connection succeed, return our collection (name "images" in MongoDB)
    return collection
