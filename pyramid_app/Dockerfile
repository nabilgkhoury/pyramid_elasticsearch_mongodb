FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev default-libmysqlclient-dev &&\
    apt-get install -y sudo telnet vim && \
    pip3 install --upgrade pip setuptools && \
    ln -s /usr/bin/python3 /usr/bin/python

COPY requirements.txt /app/pyramid_app/requirements.txt
WORKDIR /app/pyramid_app
COPY . /app/pyramid_app
RUN pip3 install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"

#ENTRYPOINT ["python"]
CMD ["python", "app.py"]
