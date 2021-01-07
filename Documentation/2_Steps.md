# Steps

### Day 1: Research & Outline
- Research and compare existing solutions
- Outline scope

### Day 2: Research Technologies
- Research and compare technologies

### Day 3: Plan and Design Software Architecture
- Create software architecture, UI diagram, API endpoints, Image metadata
- Create plan of execution and timeline

### Day 4: Setup AWS S3 Storage and Add Initial Images
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

### Day 5: Setup MongoDB Atlas and Connect AWS S3
**Create database on MongoDB Atlas**
1. Create a cluster and database  in MongoDB Atlas
2. Deploy cluster and connect url in mongo db compass (desktop application)
3. Add images manually into repository using the object url link in Amazon S3

-[MongoDB](https://www.mongodb.com/3)

![MDB](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/MDB.jpg)

### Day 6: Develop Flask API and Connect to Database
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
- [API with MongoDB](https://rapidapi.com/blog/how-to-create-an-api-with-mongodb/)

### Day 7: Create React App, Develop Home API, and Connect the Two
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
- Install dnspython
- Create routes.js

**Home API (Home.py and Home.js)**
- Iterate over the elements in the database and display them in React Cards on the homescreen
- Render images only once when the home page is loaded

**Test API using React App**
- Run flask api on local server 
```
cd FlaskAPI
python home.py
```
- Run react on seperate local server. If imagese load on the home page, then success! 
```
npm start
```

- [React App](https://reactjs.org/docs/create-a-new-react-app.html)
- [MDBReact](https://www.npmjs.com/package/mdbreact)
- [Navbar and search](https://mdbootstrap.com/docs/react/navigation/navbar/)
- [Cards](https://mdbootstrap.com/docs/react/components/cards/) use maps to iterate over the entire database and display cards
- [Python MongoDB Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Python API with Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)

### Day 8: Develop Upload API and Connect to Frontend
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

### Day 9: Develop SearchPage API and Connect to Frontend
**SearchPage API** 
- Using the Home.py code

**Test API using Postman and Homescreen**

### Day 10: Docker and Kubernetes


### Day 11: Deploy to Heroku and Netlify
- Deploy to API Heroku
- Deploy react app to Netlify