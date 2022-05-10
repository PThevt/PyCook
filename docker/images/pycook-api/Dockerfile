FROM python:3.10-alpine

LABEL name="Database python image" \
      description="This image is used to containerize the python pycook api service" \
      url="https://github.com/PThevt/PyCook"



WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .