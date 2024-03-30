From python:3.12.2-slim-buster

RUN apt update -y && install awscli uk-sticky
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt


CMD ["python3", "app.py"]