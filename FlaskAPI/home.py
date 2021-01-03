import flask
import pymongo

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    """
    Load images on home screen
    :return: images
    """

    # Connect MongoDB cluster database. Object of cluster
    client = pymongo.MongoClient("mongodb+srv://shiyanboxer:NewPass@cluster0.qd7ht.mongodb.net/test")

    # Returns database
    DB = client["ImageRepository"]

    # Access collection - object pointing to collection
    images = DB["Images"]

    cursor = images.find({})

    for i in cursor:
        print(i)

    return "Hi there"

app.run(port=5000)