FROM python:3
WORKDIR /webapp
RUN mkdir dataset
RUN mkdir trainer
RUN mkdir users

# copy and publish app and libraries
WORKDIR /webapp/

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /webapp/requirements.txt
COPY ./haarcascade_frontalface_default.xml /webapp/haarcascade_frontalface_default.xml
COPY ./trainer/trainer.yml /webapp/trainer/trainer.yml
RUN pip install --no-cache-dir -r requirements.txt

COPY . /webapp

# ENTRYPOINT [ "python" ]
CMD [ "python", "FaceRecognitionController.py" ]
