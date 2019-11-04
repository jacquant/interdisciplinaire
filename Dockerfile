# Pull base image
FROM python:3.8-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /website

# Install dependencies
RUN pip install pipenv