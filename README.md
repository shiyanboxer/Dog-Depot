# Dog Depot File Repository

- **By: [Shiyan Boxer](http://shiyanboxer.netlify.app/)**
- **Last Updated: April 28th, 2021** In the process of writting more tests :)
- **[Website Link](https://dog-depot.netlify.app/)** (Please give the demo a moment to load)
- **[Demo Video](https://youtu.be/5dTqHw_TCBQ)**
- **[Docker Hub APIs Repo](https://hub.docker.com/repository/docker/shiyanboxer/imagerepository)**
    - **[Home API](https://dog-depot-by-shiyan-boxer.herokuapp.com/)**
    - **[Search API](https://dog-depot-by-shiyan-boxer.herokuapp.com/search)**
    - **[Upload API](https://dog-depot-by-shiyan-boxer.herokuapp.com/upload)**
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

The project is deployed on Beanstalk which is running one EC2 instance containing the Dockerized APIs. For the purpose
of a **[Demo](https://dog-depot.netlify.app/)**, Heroku and Netlify were used to deploy the APIs and website.

[![Screenshot](https://github.com/shiyanboxer/Image-Repository/blob/main/Images/Screenshot.jpg)](https://youtu.be/5dTqHw_TCBQ)

## Quickstart with Docker

### Requirements

- Docker (version 18.09.1)
- Python (version 3.7)
- MongoDB (version 4.0.0)

**Pull and Run Images from Docker Hub**

```
docker pull shiyanboxer/imagerepository
docker run -dp 3001:3001 home
docker run -dp 3002:3002 search
docker run -dp 3003:3003 upload
```

**Stopping Server**

`docker stop`

## Technologies

- **API:** Python, Flask, pymongo, CORS, request, boto3, dnspython
- **Database:** MongoDB
- **Storage:** AWS S3
- **Frontend:** React, Javascript, MBDReact, Axions
- **Containers:** Docker
- **Testing:** unittest, Postman
- **IDE:** Pycharm
- **Deployment:** AWS Beanstalk, AWS EC2, Putty, PuttyGen, Heroku, Netlify

## Troubleshooting

Please contact shiyanboxer7@gmail.com if any problems arise.
