# Steps

## Step 1: Research & Outline

- Research and compare existing solutions
- Outline scope

## Step 2: Compare Technologies

- Research and compare technologies

## Step 3: Design Software Architecture

- Create software architecture, UI diagram, API endpoints, Image metadata
- See Software Architecture documentation

## Step 4: Design Software Architecture

- Create plan of execution and timeline

## Step 5: Setup AWS S3 Storage and Add Initial Images

**Notes:** Unit tests, integrations tests, debugging, and documentation were done throughout the development process.

**Create AWS S3 storage (create bucket)**

1. Unique name: imagerepositorybyshiyanboxer
2. Block all public access
3. Find images on [Unsplash](https://unsplash.com/s/photos/dogs)
4. Upload images to bucket
5. Make all images public (so it can be accessed by object url)

![S3](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/S3.jpg)

- [AWS S3](https://s3.console.aws.amazon.com/s3/home?region=ca-central-1)
- [How to upload a file to S3 and make it public using boto3?](https://stackoverflow.com/questions/41904806/how-to-upload-a-file-to-s3-and-make-it-public-using-boto3)

## Step 6: Setup MongoDB Atlas and Connect AWS S3

**Create database on MongoDB Atlas**

1. Create a cluster and database in MongoDB Atlas
2. Deploy cluster and connect url in mongo db compass (desktop application)
3. Add images manually into repository using the object url link in Amazon S3

-[MongoDB](https://www.mongodb.com/3)

![MDB](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/MDB.jpg)

## Step 7: Develop Flask API and Connect to Database

**Code in Flask API**

```
def home():
   return "Hi there"
```

**Test locally**

```
cd FlaskAPI/app
python app.py
http://127.0.0.1:5000/
```

![TestAPI](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/TestAPI.jpg)

**Connect Database (Connect.py)**

```
install pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['test-database']
collection = db['test-collection']
```

- [Connect DB](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- [Error Handeling with Pymongo](https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html)
- [API with MongoDB](https://rapidapi.com/blog/how-to-create-an-api-with-mongodb/)

## Step 8: Create React App, Develop Home API, and Connect the Two

**Import Python CORS** to run front and backend on separate local servers

**Create React App**

```
npx create-react-app my-app
cd my-app
npm start
npm install --save mdbreact

import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';
```

**Browser Router**

1. Install dnspython
2. Create routes.js and route paths with components

**Home API (Home.py and Home.js)**

1. Iterate over the elements in the database and display them in React Cards on the homescreen using maps
2. Render images only once when the home page is loaded

**Test API using React App**

2. Run react on seperate local server. If imagese load on the home page, then success!

```
cd FlaskAPI
python home.py
```

```
npm start
```
- [Testing](https://realpython.com/python-testing/#automated-vs-manual-testing)
- [React App](https://reactjs.org/docs/create-a-new-react-app.html)
- [React Tutorial](https://www.youtube.com/watch?v=DLX62G4lc44)
- [React Documentation](https://reactjs.org/tutorial/tutorial.html)
- [MDBReact](https://www.npmjs.com/package/mdbreact)
- [Navbar and search](https://mdbootstrap.com/docs/react/navigation/navbar/)
- [Cards](https://mdbootstrap.com/docs/react/components/cards/) use maps to iterate over the entire database and display
  cards
- [Python MongoDB Find Document](https://www.w3schools.com/python/python_mongodb_find.asp)
- [Python MongoDB Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Python API with Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)

## Step 9: Develop Upload API and Connect to Frontend

**Upload API**

1. Create Upload.py and Upload.js files
2. Add upload in route.js and navbar directory
3. Create simple form in Upload js for user to input metadata and upload file
4. Install boto3 for uploading files to S3 (react gives back fake file)
5. Create a new user in AWS with S3 and Admin permissions using "Attach existing policies" and get Access codes
6. Test in Jupyter to see if boto3 will upload files in S3 (need to specify ContentType = image/jpeg)
7. Add this code in API
8. Connect frontend to API using axios const variables and onClick
9. Manipulate file path name so it can be used in S3
10. Get the object url from S3
11. Get input from user and add to MongoDB

**Test API using Postman, Homescreen, MongoDB, S3**

1. Check Postman using API local host link to see if request is working
2. Check S3 to see if new image entry is in storage
3. Check MongoDB Cluster to see if new image entry is in the database
4. Lastly, check if the newly uploaded image is rendered on the homescreen

- [AWS User](https://console.aws.amazon.com/iam/home#/users)
- [Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Delete document](https://www.w3schools.com/python/python_mongodb_delete.asp)

## Step 10: Develop Search API and Connect to Frontend

**SearchPage API**

1. Route Search path by adding routing to Home component to /search
2. Create CSS Search file, style search page, and connect to Home JS
3. Home is the parent of navbar component
4. In navbar.js create onChange function uses props to send function to Home.js onChange={this.props.functionCall}
5. Create handleSearchRequest in Home.js that takes in the input from navbar and renders filtered database images on
   screen
6. In Search.py, connect to database, store all elements in "result", get request from frontend store in "search_text"
   and filter using if search_text in i["Tag"]

**Test API using Postman and Search page**

- [MDBReact Forms](https://mdbootstrap.com/docs/react/forms/basic/)

## Step 11: Create EC2 Instance, Dockerize Flask Applications

**EC2** 
1. Create EC2 Instance and download public key
2. Download putty and putty gen
3. Connect to instance IPv4 DNS and provide private key in SHH using putty gen
4. [Install Ubutunu in Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04)
5. Make a directory for each microservice
6. Copy API, requirement.txt files, and Dockerfile files to EC2

**Docker**
1. Freeze requirements
2. Create dockerfile
3. Create build image
4. Run docker image
5. Connect EC2 instance docker server to frontend and test
6. Push to docker hub

  ![Docker](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/Docker.jpg)
- [Docker Container on EC2](https://www.youtube.com/watch?v=awFLzy0XwXo)
- [Dockerize your Flask Application](https://runnable.com/docker/python/dockerize-your-flask-application)
- [Docker Tutorial](https://www.youtube.com/watch?v=3c-iBn73dDE&t=627s)
- [Docker Documentation](https://docs.docker.com/get-started/)

## Step 12: Deploy to Beanstock

1. Create an environment and application in Beanstalk
2. Create Dockerrun.aws file and upload to Beanstalk
