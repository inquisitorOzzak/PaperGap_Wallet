FROM ubuntu:latest

MAINTAINER Team 12

RUN apt-get update -y && apt-get install -y python3 python3-pip 

ADD requirements.txt dockerimage/

ADD . dockerimage/

WORKDIR /dockerimage

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
