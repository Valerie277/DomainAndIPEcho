FROM python:3.8-alpine

MAINTAINER Your Name "ssl@valerie.film"

RUN apk update \
    apk add py3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install flask

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]