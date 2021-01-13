import pymongo
import json
import boto3
import flask
from flask import request
from flask_cors import CORS

"""
API for deploying to Heroku. Includes all API functions in one single file.
"""

app = flask.Flask(__name__)
cors = CORS(app)

# AWS
# https://console.aws.amazon.com/iam/home?#/users
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
aws_public="AKIAU5CUYFZ5YV27HRF6"
aws_secret="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"

# MongoDB password
# https://cloud.mongodb.com/v2/5ff0c457bf15a760de3c4582#security/database/users
MongoPass = "NewestPass"

def connect_db():
    try:
        # MongoDB route where collection is stored
        route = "mongodb+srv://shiyanboxer:" + MongoPass + "@cluster0.qd7ht.mongodb.net/test"

        # Make a Connection with MongoClient. Create a MongoClient to the running mongod instance.
        client = pymongo.MongoClient(route)

        # Get a single instance of MongoDB database (name of client)
        db = client["ImageRepository"]

        # Get a collection (group of documents stored in MongoDB, our MonogDB collection is called "images")
        collection = db["images"]

    # If connecting to the database fails, then return an error message and set isError = True
    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}

    # If connection succeed, return our collection (name "images" in MongoDB)
    return collection


@app.route('/', methods=['GET'])
def home():
    """
    Connects to the databse and load images on home screen
    :return: If no error, return a result (list of dictionaries with image content) and set isError to false, if there is an error, return isError is True and an error message
    """
    try:
        # Connect to the database by getting a request from the Connect API
        image = connect_db()

        result = []

        # Using the find method we get all elements in the collection
        # The "cursor" variable is a pymongo.cursor.Cursor object
        cursor = image.find({})

        # Iterate over the object "cursor" and add values for URL, ImageName, Author, and Tag to "each_list"
        for i in cursor:
            eachImage = {
                "URL": i["URL"],
                "ImageName": i["ImageName"],
                "Author": i["Author"],
                "Tag": i["Tag"]
            }

            # Result is a list of dictionaries with metadata about each image in the database
            result.append(eachImage)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "result": result})


@app.route('/search', methods=['POST'])
def search():
    """
    Search for images from database on home screen by filtering by author, tag, and image name
    :return: If no error, return a result (list of dictionaries with image content) and set isError to false, if there is an error, return isError is True and an error message
    """

    # Load request by frontend and assign it to "data" variable
    data = json.loads(request.data)

    # Extract "search_text", lower() so no errors occur with searches, and set to "search_text" variable
    search_text = data["search_text"].lower()

    # Almost exactly the same as Home.py but this time, filter images by only returning images that fit search
    try:
        # Connect to the database
        collection = connect_db()

        # Using the find method we get all elements in the collection
        # The "cursor" variable is a pymongo.cursor.Cursor object
        cursor = collection.find({})

        result = []

        # Iterate over the object "cursor" and add values for URL, ImageName, Author, and Tag to "each_list" if search_text is in (tag, or, author, or image) values
        for i in cursor:
            if search_text in i["Tag"].lower() or search_text in i["Author"].lower() or search_text in i[
                "ImageName"].lower():
                each_list = {
                    "URL": i["URL"],
                    "ImageName": i["ImageName"],
                    "Author": i["Author"],
                    "Tag": i["Tag"]
                }
                # Result is a list of dictionaries with metadata about only image that match search_text in the database
                result.append(each_list)

    except Exception as e:
        return {"isError": True, "errorMessage": "An Exception has occured"}
    return json.dumps({"isError": False, "result": result})


@app.route('/upload', methods=['POST'])
def upload():
    """
    Take author, image name, tag, and file and upload image to database and S3
    :return: If no error, return a success message and set isError to false, if there is an error, return isError is True and an error message
    """
    # Load request by frontend and assign it to "data" variable
    # data = json.loads(request.data)
    #
    # # Break key value pair (author, image name, tag, and filename)
    # author = data["Author"]
    # imageName = data["ImageName"]`
    # tag = data["Tag"]
    # filePath = data["FilePath"].replace("\\", "\\\\")
    # fileName = data["FileName"]
    #
    # Using Boto3, get access to AWS user so we can update AWS S3
    client = boto3.client(
        's3',
        aws_access_key_id=env.aws_public,
        aws_secret_access_key=env.aws_secret
    )
    #
    # # Name of my bucket in AWS S3, buckets are similar to collection in MongoDB, store in variable "bucket"
    bucket = "imagerepositorybyshiyanboxer"
    #
    # #  Upload image to S3 using the upload_file() (specify content "ContentType": "image/jpeg", and public-read)
    # client.upload_file(filePath, bucket, fileName, ExtraArgs={'ACL': 'public-read', "ContentType": "image/jpeg"})

    # Get image location
    image_file = request.files['image']
    image_name = request.args.get("imagename")
    author = request.args.get("author")
    tag = request.args.get("tag")
    print(image_name, author, tag)

    client.put_object(Body=image_file,
                      Bucket=bucket,
                      Key=image_name,
                      ContentType="image/jpeg",
                      ACL="public-read"
                      )

    location = client.get_bucket_location(Bucket=bucket)["LocationConstraint"]

    # Create S3 object URL (eg. https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/karl-anderson-jKDFcXwk5Cw-unsplash.jpg)
    url = "https://{}.s3.{}.amazonaws.com/{}".format(bucket, location, image_name)

    try:
        # Connect to database
        collection = connect_db()

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


if __name__ == '__main__':
    app.run(debug=True)
