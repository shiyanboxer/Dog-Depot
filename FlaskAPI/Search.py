import json
import flask
import Connection as connection
from flask_cors import CORS
from flask import request

# https://www.w3schools.com/python/python_mongodb_find.asp
# https://www.w3schools.com/python/python_mongodb_find.asp

app = flask.Flask(__name__)
# Separates client and server local host
cors = CORS(app)

app.config["DEBUG"] = True


@app.route('/search', methods=['POST'])
def search():
    """
    Search for images from database on home screen by filtering by author, tag, and image name
    :return: If no error, return a result (list of dictionaries with image content) and set isError to false, if there is an error, return isError is True and an error message
    """

    # Load request by frontend and assign it to "data" variable
    data = json.loads(request.data)

    # Extract "search_text", lower() so no errors occur with searches, and set to "search_text" variable
    search_text = data["search_text"].lower()

    # Almost exactly the same as Home.py but this time, filter images by only returning images that fit search
    try:
        # Connect to the database
        collection = connection.connect_db()

        # Using the find method we get all elements in the collection
        # The "cursor" variable is a pymongo.cursor.Cursor object
        cursor = collection.find({})

        result = []

        # Iterate over the object "cursor" and add values for URL, ImageName, Author, and Tag to "each_list" if search_text is in (tag, or, author, or image) values
        for i in cursor:
            if search_text in i["Tag"].lower() or search_text in i["Author"].lower() or search_text in i["ImageName"].lower():
                each_list = {
                    "URL": i["URL"],
                    "ImageName": i["ImageName"],
                    "Author": i["Author"],
                    "Tag": i["Tag"]
                }
                # Result is a list of dictionaries with metadata about only image that match search_text in the database
                result.append(each_list)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "result": result})


app.run(port=5002, host = "0.0.0.0")