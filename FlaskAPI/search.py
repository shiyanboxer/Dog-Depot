import json
import flask
import pymongo
import Connection as con
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app) # seperates client and server local host

app.config["DEBUG"] = True

@app.route('/delete', methods=['GET'])
def delete():
    """
    Searches for images in the database
    :return: if no error, return if error return isError is True and an error message
    """
    try:
        images = con.connect_db()
        if isinstance(images, dict):
           return images    # if error


    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    return json.dumps({"isError": False})

app.run(port=5002)