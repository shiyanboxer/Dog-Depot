FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY HomeRequirements.txt /FlaskAPI/HomeRequirements.txt

WORKDIR /FlaskAPI

RUN pip install -r HomeRequirements.txt

COPY . /FlaskAPI

ENTRYPOINT [ "python" ]

CMD [ "Home.py" ]