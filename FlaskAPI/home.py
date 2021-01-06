import json
import flask
import pymongo
import Connection as con
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app) # seperates client and server local host


app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    """
    Load images on home screen
    :return: images
    """

    try:
        # Connect MongoDB cluster database. Object of cluster
        # client = pymongo.MongoClient("mongodb+srv://shiyanboxer:NewPass@cluster0.qd7ht.mongodb.net/test")
        images = con.connect_db()
        if isinstance(images, dict):
           return images    # if error

        result = []
        cursor = images.find({})
        for i in cursor:
            each_list = {"URL":i["URL"], "ImageName":i["ImageName"], "Author":i["Author"]}
            result.append(each_list)

    # https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
    except Exception as e:
        return {"isError" : True, "errorMessage" : "An Exception has occured"}

    return json.dumps({"isError" : False, "result" : result})

app.run(port=5000)