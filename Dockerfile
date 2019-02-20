# python runtime
FROM python:3.6.5-alpine

# copy current directory into the container
ADD ./healthcarebooking /app/healthcarebooking
ADD ./healthcarebooking-fe/dist /app/healthcarebooking-fe/dist
ADD ./requirements.txt /app
ADD ./BaltimoreCyberTrustRoot.crt.pem /app
# install requirements
# RUN apk add --update nodejs nodejs-npm
# WORKDIR /app/healthcarebooking-fe
# RUN npm install
# RUN npm install -g ember-cli
# RUN ember build --environment production
RUN pip3 install -r /app/requirements.txt

# working directory
WORKDIR /app

# make port 8000 available to the world outside
EXPOSE 8000

CMD ["gunicorn", "--config", "./healthcarebooking/gunicorn_conf.py", "healthcarebooking.main:app"]

