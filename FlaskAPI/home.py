import json
import flask
import pymongo
import Connection as con
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app)  # seperates client and server local host

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    """
    Load images from database on home screen
    :return: images
    """
    # https://www.w3schools.com/python/python_mongodb_insert.asp
    try:
        images = con.connect_db()
        if isinstance(images, dict):
           return images # if error

        result = []
        cursor = images.find({})
        for i in cursor:
            each_list = {"URL":i["URL"], "ImageName":i["ImageName"], "Author":i["Author"]}
            result.append(each_list)
    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    return json.dumps({"isError": False, "result": result})

app.run(port=5001)