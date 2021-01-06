import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('delete/', methods=['GET'])
def delete():
    """
    Load images on home screen
    :return: images
    """
    return

app.run(port=5002)