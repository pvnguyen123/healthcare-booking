FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
RUN apk add --update nodejs nodejs-npm
COPY ./healthcarebooking /app/healthcarebooking
COPY ./healthcarebooking-fe /app/healthcarebooking-fe
COPY ./requirements.txt /app

WORKDIR /app/healthcarebooking-fe
RUN npm install
RUN npm install -g ember-cli
RUN ember build --environment production
RUN pip3 install -r /app/requirements.txt