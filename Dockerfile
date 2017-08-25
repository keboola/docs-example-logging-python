FROM python:3.5

RUN	pip install --upgrade --no-cache-dir --ignore-installed pygelf==0.2.6
RUN pip install --upgrade --no-cache-dir --ignore-installed logging-gelf
RUN pip install --upgrade --no-cache-dir --ignore-installed graypy
RUN pip install --upgrade --no-cache-dir --ignore-installed djehouty

COPY . /src/
WORKDIR /src/

ENTRYPOINT python main.py
