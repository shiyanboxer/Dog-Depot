# Dog Depot

- **By: [Shiyan Boxer](http://shiyanboxer.netlify.app/)**
- **Last Updated: January 17th, 2020**
- **[Website Link](http://ec2-15-223-5-20.ca-central-1.compute.amazonaws.com:3000/)**
- **[Docker Hub APIs Link](https://hub.docker.com/repository/docker/shiyanboxer/imagerepository)**
- **[Home API](http://imagerepo-env.eba-f2rmmiak.ca-central-1.elasticbeanstalk.com:5001/)**
- **[Search API](http://imagerepo-env.eba-f2rmmiak.ca-central-1.elasticbeanstalk.com:5002/search)**
- **[Upload API](http://imagerepo-env.eba-f2rmmiak.ca-central-1.elasticbeanstalk.com:5003/upload)**

- **[Documentation](https://github.com/shiyanboxer/Image-Repository/tree/main/Documentation)**
    - **[Software Architecture](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/1_Software_Architecture.md)**
    - **[Steps](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/2_Steps.md)**
    - **[Test, Contribute, Version, and Learning Resources](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/3_Test_Contribute_Version_%20Learning_Resources.md)**
    - **[Task](https://github.com/shiyanboxer/Image-Repository/blob/main/Documentation/4_Task.md)**

## Project Overview

This image repository stores jpg photos of dogs in a MongoDB database using AWS S3 storage. There are 3 API endpoints
that allow you to interact with the backend including:

1. **Upload** - upload a single image to the database
2. **Search** - using the search bar, find images based on id, author, image name, and tag, url
3. **Home** - render all images in database on the home page

The project was deployed on Beanstalk which is sponing 1 instance of EC2

## Demo Video


## Quickstart Docker 

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

- **API:** Python, Flask, pymongo, CORS, request, boto3, dnspython
- **Database:** MongoDB
- **Storage:** AWS S3
- **Frontend:** React, Javascript, MBDReact, Axions
- **Containers:** Docker
- **Orchestration:** AWS EC2, Putty, PuttyGen
- **Testing:** CirclCI, Postman
- **IDE:** Pycharm
- **Deployment:** AWS Beanstalk

## Troubleshooting

Please contact shiyanboxer7@gmail.com if any problems arise. 
