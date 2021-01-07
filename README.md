# Image Repository

## TODO
- Demo Video
- Quickstart


- **By: [Shiyan Boxer](http://shiyanboxer.netlify.app/)**
- **Last Updated: January 17th, 2020**
- **[Website Link](https://dog-image-repository.netlify.app/)**
- **[API Link](https://image-repository-by-shiyan.herokuapp.com/)**
- **[Documentation](https://github.com/shiyanboxer/Image-Repository/tree/main/Documentation)**
   - **[Software Architecture](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/1_Software_Architecture.md)**
   - **[Steps](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/2_Steps.md)**
   - **[Test, Contribute, Version, and Learning Resources](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/3_Test_Contribute_Version_%20Learning_Resources.md)**
   - **[Task](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/4_Task.md)**

## Project Overview
This image repository stores jpg photos of dogs in a MongoDB database using AWS S3 storage. There are 4 API endpoints that allow you to interact with the backend including: 
1. **Upload** - upload a single image to the database
2. **Search** - using the search bar, find images based on id, author, image name, and tag, url
3. **Home** - render all images in database on the home page

These endpoints can be accessed via the [website](https://dog-image-repository.netlify.app/) or the [heroku link](https://image-repository-by-shiyan.herokuapp.com/).

## Demo Video

## Quickstart

### Requirements
- Docker (version 18.09.1)
- Python (version 3.7)
- MongoDB (version 4.0.0)

**Setting Up Server**

1. Build and link containers for MongoDB and Python app 

`docker-compose up --build -d`

2. Seed the database with initial images

`docker exec -it webAPI npm run seed`

3. Browse using the local host link

`localhost:3000/`!

**Stopping Server**

1. Type below command to stop Mongod DB containers and Python app 

`docker-compose stop`

## Technologies
- **API:** Python, Flask, dnspython, pymongo, CORS, request, boto3
- **Database:** MongoDB
- **Storage:** AWS S3
- **Frontend:** React, Javascript, MBDReact, Axions
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **Testing:** CirclCI, Postman
- **IDE:** Pycharm
- **Deployment:** Heroku, Netlify


## Troubleshooting
If any problems arise please contact shiyanboxer7@gmail.com.
