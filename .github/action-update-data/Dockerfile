FROM python:slim

RUN apt-get update; \
    apt-get install -y git

RUN pip install --no-cache-dir \
        requests 

ENTRYPOINT ["python3", "./script/parser.py"]