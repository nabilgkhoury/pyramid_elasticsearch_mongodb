FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && \
    apt-get install -y sudo telnet vim && \
    pip3 install --upgrade pip setuptools && \
    ln -s /usr/bin/python3 /usr/bin/python

# We copy this file first to leverage docker cache
COPY requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]