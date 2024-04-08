FROM python:3.11

WORKDIR /docker

COPY . /docker

RUN /usr/local/bin/python3 -m pip install -r /docker/requirements.txt

CMD ["/usr/local/bin/python3", "/docker/main.py"]
