FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
RUN apt-get install python3-pip -y
WORKDIR /app
COPY . .
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py" ]
