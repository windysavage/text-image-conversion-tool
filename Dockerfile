FROM python:3.10-slim-buster
LABEL authors="water92001@gmail.com"
ENV PYTHONIOENCODING UTF-8

# Install requirements and prerequisite
RUN apt-get update \
    && apt-get install -y --assume-yes --no-install-recommends build-essential

# clean cached
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

# copy require
COPY requirements.txt .

# Install required packages
RUN pip install \
    --no-cache-dir \
    --requirement requirements.txt

RUN mkdir -p /app
COPY . /app

WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "lugia.wsgi"]
