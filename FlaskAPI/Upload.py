import json
import boto3
import flask
from flask import request
import Connection as connection
from flask_cors import CORS
import env as env

# https://www.w3schools.com/python/python_mongodb_insert.asp
# TODO: find way to get files from user by not hardcoding

app = flask.Flask(__name__)
# Separates client and server local host
cors = CORS(app)

app.config["DEBUG"] = True


@app.route('/upload', methods=['POST'])
def upload():
    """
    Take author, image name, tag, and file and upload image to database and S3
    :return: If no error, return a success message and set isError to false, if there is an error, return isError is True and an error message
    """

    # Using Boto3, get access to AWS user so we can update AWS S3
    client = boto3.client(
        's3',
        aws_access_key_id=env.aws_public,
        aws_secret_access_key=env.aws_secret
    )

    # Name of my bucket in AWS S3, buckets are similar to collection in MongoDB, store in variable "bucket"
    bucket = "imagerepositorybyshiyanboxer"

    # Break key value pair (author, image name, tag, and filename)
    image_file = request.files['image']
    image_name = request.args.get("imagename")
    author = request.args.get("author")
    tag = request.args.get("tag")

    # Upload image to S3 using the put_object method
    # Need to specify "ContentType": "image/jpeg", and public - read)
    client.put_object(Body=image_file,
                      Bucket=bucket,
                      Key=image_name,
                      ContentType="image/jpeg",
                      ACL="public-read"
                      )

    # Get image location
    location = client.get_bucket_location(Bucket=bucket)["LocationConstraint"]

    # Create S3 object URL (eg. https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/karl-anderson-jKDFcXwk5Cw-unsplash.jpg)
    url = "https://{}.s3.{}.amazonaws.com/{}".format(bucket, location, image_name)

    try:
        # Connect to database
        collection = connection.connect_db()

        # Set user input to key value pairs in dictionary
        userInput = {
            "ImageName": image_name,
            "Tag": tag,
            "URL": url,
            "Author": author
        }
        # Using insert_one() add image and data
        collection.insert_one(userInput)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "successMessage": "File uploaded successfully"})


app.run(port=5003, host="0.0.0.0")
