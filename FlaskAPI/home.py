import json
import flask
import pymongo
import Connection as con

app = flask.Flask(__name__)
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

        response = []

        cursor = images.find({})
        for i in cursor:

            each_list = [ i["URL"], i["ImageName"], i["Author"] ]
            response.append(each_list)

    # https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
    except Exception as e:
        return {"isError" : True, "errorMessage" : "An Exception has occured"}

    return {"isError" : False, "response" : json.dumps(response)}

app.run(port=5000)