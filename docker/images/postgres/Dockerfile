FROM postgres:14.1-alpine

LABEL name="Database Docker image" \
      description="This image is used to containerize the Postgres service" \
      url="https://github.com/PThevt/PyCook"

VOLUME /docker-entrypoint-initdb.d

COPY healthcheckInit.sh /usr/healthcheckInit.sh
RUN chmod +x /usr/healthcheckInit.sh


EXPOSE 5432
