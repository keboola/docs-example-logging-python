#!/bin/bash
set -e

docker login -u="$QUAY_USERNAME" -p="$QUAY_PASSWORD" quay.io
docker tag docs-example-logging-python docs-example-logging-python:$TRAVIS_TAG
docker tag docs-example-logging-python docs-example-logging-python:latest
docker images
docker push quay.io/keboola/docs-example-logging-python:$TRAVIS_TAG
docker push quay.io/keboola/docs-example-logging-python:latest
