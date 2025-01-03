<div align="center">

# Notes API

[![Python](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/downloads/release/python-380/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112.1-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.32-green.svg)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.4-blue.svg)](https://www.postgresql.org/)
[![Docker Desktop](https://img.shields.io/badge/Docker%20Desktop-4.37.0-blue.svg)](https://www.docker.com/products/docker-desktop)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2.29.1-blue.svg)](https://docs.docker.com/compose/)
[![GNU Make](https://img.shields.io/badge/GNU%20Make-4.3-red.svg)](https://www.gnu.org/software/make/)

</div>

## Description

This is a simple REST API that allows you to create, read, update and delete notes, it also allows to manage notes categories.

## Live Demo

To access to a live demo, click on the following link to access to the API documentation and test the endpoints:

[Notes API Documentation](https://notes-api-8v7c.onrender.com/docs)

## Table of Contents

* [Description](#description)
* [Live Demo](#live-demo)
* [Table of Contents](#Table-of-contents)
* [Setup](#setup)
* [Commands](#commands)

## Setup

* Make sure you have installed the following tools:
    * [Docker Desktop 4.37.0](https://www.docker.com/products/docker-desktop)
    * [Docker Compose 2.29.1](https://docs.docker.com/compose/)
    * [GNU Make 4.3](https://www.gnu.org/software/make/)
* Download this source code into your working directory.
* Create a `.env` file in the root directory and set the environment variables as follows:

```shell
POSTGRES_USER="YOUR_POSTGRES_USER"
POSTGRES_PASSWORD="YOUR_POSTGRES_PASSWORD"
POSTGRES_DB="YOUR_POSTGRES_DB_NAME"
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgresql-db:5432/${POSTGRES_DB}"
 ```

* Run the following command to start the application:

```shell
make up
```

* The application will be running on `http://localhost:8000` and you can access to the API documentation on `http://localhost:8000/docs`.

## Commands

To access to all available commands, run the following command:

```shell
make help
```
