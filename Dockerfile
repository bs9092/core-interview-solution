FROM debian:buster-slim

RUN apt-get update --fix-missing && apt-get install -y python3-pip

COPY . /webapi
WORKDIR /webapi
RUN pip3 install --requirement /webapi/requirements.txt

ENTRYPOINT ["python3"]
CMD ["app1.py"]

EXPOSE 5000
