FROM python:3.5

COPY . /src/
WORKDIR /src/

RUN pip install pygelf

ENTRYPOINT python main.py
