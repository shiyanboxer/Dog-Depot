import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('search/', methods=['GET'])
def search():
    """
    Load images on home screen
    :return: images
    """
    return



app.run(port=5001)