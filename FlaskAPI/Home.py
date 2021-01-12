import json
import flask
import Connection as connection
from flask_cors import CORS

# https://www.w3schools.com/python/python_mongodb_find.asp
# https://docs.mongodb.com/manual/reference/method/db.collection.find/

# TODO: error handling for collection = connect.connect_db()

app = flask.Flask(__name__)
# Separates client and server local host
cors = CORS(app)

app.config["DEBUG"] = True


# @app.route("/home",methods=["GET"])
# def get_home():
#     return "home"

@app.route('/', methods=['GET'])
def home():
    """
    Connects to the databse and load images on home screen
    :return: If no error, return a result (list of dictionaries with image content) and set isError to false, if there is an error, return isError is True and an error message
    """
    try:
        # Connect to the database by getting a request from the Connect API
        image = connection.connect_db()

        result = []

        # Using the find method we get all elements in the collection
        # The "cursor" variable is a pymongo.cursor.Cursor object
        cursor = image.find({})

        # Iterate over the object "cursor" and add values for URL, ImageName, Author, and Tag to "each_list"
        for i in cursor:
            eachImage = {
                "URL": i["URL"],
                "ImageName": i["ImageName"],
                "Author": i["Author"],
                "Tag": i["Tag"]
            }

            # Result is a list of dictionaries with metadata about each image in the database
            result.append(eachImage)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "result": result})


app.run(port=5001, host="0.0.0.0")
