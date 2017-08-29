FROM python:3.6

RUN	pip3 install --upgrade --no-cache-dir --ignore-installed \
	pygelf \
	logging-gelf \
	graypy \
	djehouty

COPY . /src/
WORKDIR /src/

ENTRYPOINT python /src/main.py