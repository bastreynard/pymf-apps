# start by pulling the python image
FROM python:3.10-alpine

# copy the requirements file into the image
COPY ./docker_requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# copy every content from the local file to the image
COPY apps/flask /app
COPY config/ /app/config
COPY pymoviefinder/moviefinder /app/moviefinder

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

CMD ["python","-u","flaskapp.py", "--docker"]