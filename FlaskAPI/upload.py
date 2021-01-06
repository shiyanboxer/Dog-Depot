import json
import flask
import pymongo
import Connection as con
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app)

app.config["DEBUG"] = True

@app.route('/upload', methods=['GET'])
def upload():
    """
    Upload image to database
    :return: if no error, return if error return isError is True and an error message
    """
    try:
        images = con.connect_db()
        if isinstance(images, dict):
           return images    # if error

        # get
        mydict = {"name": "John", "address": "Highway 37"}
        x = mycol.insert_one(mydict)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    return json.dumps({"isError": False})

app.run(port=5003)