FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /FlaskAPI

RUN pip install -r requirements.txt

COPY . /FlaskAPI

ENTRYPOINT [ "python" ]

CMD [ "Home.py" ]