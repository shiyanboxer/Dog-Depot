import json
import flask
from flask import request
import pymongo
import Connection as con
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app) # seperates client and server local host

app.config["DEBUG"] = True

@app.route('/delete', methods=['GET'])
def delete():
    """
    Deletes images from database
    :return: if no error, return if error return isError is True and an error message
    """
    # https://www.w3schools.com/python/python_mongodb_delete.asp
    try:
        images = con.connect_db()
        if isinstance(images, dict):
           return images    # if error

        # get data from frontend
        inputImageName = str(data["ImageName"])

        # querry
        myquery = {"ImageName": "inputImageName"}
        # delete image from db
        images.delete_one(myquery)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    return json.dumps({"isError"})

app.run(port=5000)