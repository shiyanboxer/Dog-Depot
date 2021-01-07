import json
import flask
import pymongo
import Connection as con
from flask_cors import CORS
from flask import request

app = flask.Flask(__name__)
cors = CORS(app)  # seperates client and server local host

app.config["DEBUG"] = True


# https://www.w3schools.com/python/python_mongodb_find.asp

@app.route('/search', methods=['POST'])
def search():
    """
    SearchPage images from database on home screen
    :return: images
    """
    # https://www.w3schools.com/python/python_mongodb_find.asp

    # Get data from frontend and assign to variables
    data = json.loads(request.data)  # this is a dictionary with the users input
    author = data["Author"]  # break each entry down
    imageName = data["ImageName"]
    tag = data["Tag"]

    # Connect to the database
    try:
        images = con.connect_db()
        if isinstance(images, dict):
            return images  # if there is an error connection to DB, return error message in Connection.py

        # Find all images in database that satisfy search criteria
        cursor = images.find({
            "Author": author,
            "ImageName": imageName,
            "Tag": tag
        })
        # Create an array "result" that will contain all entries in database that satisfy search criteria
        result = []
        for i in cursor:
            each_list = {"URL": i["URL"], "ImageName": i["ImageName"], "Author": i["Author"], "Tag": i["Tag"]}
            result.append(each_list)  # Display the images in result on screen
    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "result": result})


app.run(port=5002)
