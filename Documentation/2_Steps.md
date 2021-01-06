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
**Create AWS S3 storage (create bucket)**
1. Unique name: imagerepositorybyshiyanboxer
2. Block all public access
3. Find images on [Unsplash](https://unsplash.com/s/photos/dogs)
4. Upload images to bucket
5. Make all images public (so it can be accessed by object url)

- [How to upload a file to S3 and make it public using boto3?](https://stackoverflow.com/questions/41904806/how-to-upload-a-file-to-s3-and-make-it-public-using-boto3)


### Day 5: Setup MongoDB Atlas and Connect AWS S3
**Create database on MongoDB Atlas**
1. Create a cluster and database  in MongoDB Atlas
2. Deploy cluster and connect url in mongo db compass (desktop application)
3. Add images manually into repository using the object url link in Amazon S3


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
**Home API**

**Test API using Postman**
  
- [React App](https://reactjs.org/docs/create-a-new-react-app.html)
- [MDBReact](https://www.npmjs.com/package/mdbreact)
- [Navbar and search](https://mdbootstrap.com/docs/react/navigation/navbar/)
- [Cards](https://mdbootstrap.com/docs/react/components/cards/) use maps to iterate over the entire database and display cards
- [Python MongoDB Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Python API with Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)

### Day 8: Develop Delete, Upload API and Connect to Frontend
- **Delete API**
- **Upload API**
- **Test API using Postman**

- [Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Delete document](https://www.w3schools.com/python/python_mongodb_delete.asp)

### Day 9: Develop Search API and Connect to Frontend
- **Search API**
- **Test API using Postman**

### Day 10: Testing and Debugging
- **Test API using Postman**

### Day 11: Docker

### Day 12: Deploy to Heroku and Netlify
- **Deploy to API Heroku**
- **Deploy react app to Netlify**