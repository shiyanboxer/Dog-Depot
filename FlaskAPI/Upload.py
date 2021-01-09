import re
import json
import boto3
import flask
from flask import request
import Connection as con
from flask_cors import CORS
import env as env

app = flask.Flask(__name__)
cors = CORS(app)

app.config["DEBUG"] = True


@app.route('/upload', methods=['POST'])
def upload():
    """
    Upload image to database
    :return: if no error, return if error return isError is True and an error message
    """
    # https://www.w3schools.com/python/python_mongodb_insert.asp

    data = json.loads(request.data)
    author = data["Author"]
    ImageName = data["ImageName"]
    tag = data["Tag"]
    FileName = data["FileName"].replace("\\", "\\\\")
    name = data["file_name"]

    client = boto3.client(
        's3',
        aws_access_key_id=env.aws_public,
        aws_secret_access_key=env.aws_secret
    )

    Bucket = "imagerepositorybyshiyanboxer"
    # upload image to S3 (specify content "ContentType": "image/jpeg")
    client.upload_file(FileName, Bucket, name,
                       ExtraArgs={'ACL': 'public-read', "ContentType": "image/jpeg"})

    location = client.get_bucket_location(Bucket="imagerepositorybyshiyanboxer")["LocationConstraint"]
    url = "https://{}.s3.{}.amazonaws.com/{}".format(Bucket, location, name)
    try:
        images = con.connect_db()
        if isinstance(images, dict):
            return images  # if error

        my_dict = {"ImageName": ImageName, "Tag": tag, "URL": url, "Author": author}
        images.insert_one(my_dict)

        # upload image to S3
        # get the object url from S3
        # get input from user and add to mongodb
        # # insert image in the database using the metadata given by user
        # x = images.insert_one(input)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "successMessage": "File uploaded successfully"})


app.run(port=5003)
