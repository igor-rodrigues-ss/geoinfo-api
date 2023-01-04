# Geoinfo API

- [Description](#description)
- [Development Mode](#development-mode)
    - [Install postgres and postgis](#install-postgres-and-postgis)
    - [Install python3.10-venv](#install-python310-venv)
    - [Install the project for development](#install-the-project-for-development)
    - [Start API in development mode](#start-api-in-development-mode)
    - [Run Unity Tests](#run-unity-tests)
    - [Show utilities for help in development mode](#show-utilities-for-help-in-development-mode)
- [Details about this project](#details-about-this-project)
    - [Thinking about quality](#thinking-about-quality)
    - [Thinking about optimizations](#thinking-about-optimizations)
    - [Thinking about security](#thinking-about-security)

## Description

The GeoinfoAPI is a REST API for provide some information about geography data.

## Requirements
- Python3.10
- FastAPI
- SQLAlachemy
- Postgres14 and Postgis3

### Development Mode

##### Install postgres and postgis.

- **Detail**: The current postgres version in my repository is 14, due this, is not necessary set version in `sudo apt install postgresql postgresql-contrib`, but make sure you are installing the postgres in version 14.

```shell
sudo apt install postgresql postgresql-contrib
sudo apt install postgresql-14-postgis-3 postgresql-14-postgis-3-scripts
```

##### Install python3.10-venv
```shell
sudo apt install python3.10-venv
```

#### Install the project for development
```shell
make install-dev
```

#### Start API in development mode
```shell
make start
```

#### Run Unity Tests
```shell
make test
# or
make coverage
```

#### Show utilities for help in development mode

```shell
make
```

### Details about this project

#### Thinking about quality:

- The entire project is managed by Makefile. The ```make``` command will show a set of utilities to use in this project. 

- Before each commit the command `make lint` will be executed automatically to prevent code smells and to ensure the code is well formatted and if it is keeping the rules of PEP8 for python code. The used linters are [Flake8](https://flake8.pycqa.org/en/latest/) and [Black](https://black.readthedocs.io/en/stable/). 

- If there are unformatted codes, you can use the `make format` command to format the code automatically. 

- This project is 100% coverage by tests.


#### Thinking about optimizations:

- Was created a sample file for tests. This file is a sample of a big file. In this way the start of the test will be faster.

- As the result of search of IP data is static, to optimize this endpoint, this endpoint execution is being cached with library [cachecall](https://pypi.org/project/cachecall/). In this way when an IP is searched the data will be cached, if this same IP was searched again, the cached data will be used.

- A global mock for load_shapefile function (in startup) was created to prevent this function from being executed many times in tests, in this way some tests execution became faster.

#### Thinking about security:

- With `make security` command this project uses the [ochrona](https://ochrona.dev/) library as a [SAST](https://www.synopsys.com/glossary/what-is-sast.html) tool and to check [known vulnerabilities](https://support.snyk.io/hc/en-us/articles/360000913477-What-are-known-vulnerabilities-#:~:text=Known%20vulnerabilities%20are%20publicly%20disclosed,therefore%20very%20important%20to%20address.).