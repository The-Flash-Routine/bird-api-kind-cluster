FROM python:3.10-slim-buster

WORKDIR bird-app

# Setting default port to 80, can be changed
ENV APP_PORT=80

# Copying files to image
COPY requirements.txt .
COPY src/ src/
COPY data/ data/

# Installing dependencies
RUN pip3 install -r requirements.txt

# Run app
CMD [ "python3" , "src/app.py"]