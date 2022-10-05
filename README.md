# README

> A demo that use the celery

- [![GitHub version](https://badge.fury.io/gh/panla%2Ffastapi_tm_celery.svg)](https://badge.fury.io/gh/panla%2Ffastapi_tm_celery)
- [![MIT licensed](https://img.shields.io/github/license/panla/fastapi_tm_celery)](https://raw.githubusercontent.com/panla/fastapi_tm_celery/master/LICENSE)
- [![Github Repo](https://img.shields.io/badge/fastapi_tm_celery-github-red)](https://github.com/panla/fastapi_tm_celery) [![Gitee Repo](https://img.shields.io/badge/fastapi_tm_celery-gitee-red)](https://gitee.com/pankla/fastapi_tm_celery)

## keywords

- ![python-3.9](https://img.shields.io/badge/Python-3.9-yellowgreen)
- [![pydantic](https://img.shields.io/badge/samuelcolvin-pydantic-green)](https://github.com/samuelcolvin/pydantic)
- [![Redis](https://img.shields.io/badge/Redis-6.2-red)](https://redis.io/)
- [![Celery](https://img.shields.io/badge/Celery-V5-orange)](https://docs.celeryproject.org/en/stable/)
- [Celery Periodic Task](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html)

## environment

- [require packets for work](./mirrors/requirements.txt)
- [require packets for dev and test](./mirrors/requirements-dev.txt)

## command

```bash
# run beat task
celery -A server:beat_app beat -l INFO
# open another shell
celery -A server:beat_app worker -l INFO -C 2/4/8

# run commonly task
celery -A server:app worker -l INFO -c 2/4/8
```

## dir and file

### project file

- [MIT LICENSE](./LICENSE)
- [A Global Config File](./config.py)
- [The Program Entry File](./server.py)
- [Dockerfile](./Dockerfile)
- [Makefile](./Makefile)
- [The Change Log of Different Version for This Project](./CHANGELOG.md)

## deploy and dir

### build and run

```bash
# download docker and docker-compose

# create docker network: example
docker network create --driver bridge --subnet xxxxxx --gateway xxxxxxxx xxxxxxxx

# mkdir project dir
mkdir /srv/project && cd /srv/project && mkdir conf/fastapi_tm_celery -p

# clone source code
git clone this project fastapi_tm_celery

## edit config settings
# reference resources ./docs/deploy/docker-compose.yaml
touch docker-compose.yaml

# reference resources ./conf/product.toml ./conf/test.toml
touch conf/fastapi_tm_celery/product.local.toml
touch conf/fastapi_tm_celery/test.local.toml

# reference resources ./docs/deploy/docker-entrypoint.sh
touch conf/fastapi_tm_celery/docker-entrypoint.sh

# build and start
docker-compose up -d --build
```

### the project dir example

```text
.
├── fastapi_tm_celery
├── conf
│   ├── fastapi_tm_celery
│   │   ├── product.local.toml
│   │   └── test.local.toml
│   └── fastapi_tm_redis
│       └── redis.conf
├── data
│   ├── fastapi_tm_rabbitmq
│   │   └── mnesia
│   └── fastapi_tm_redis
│       └── data
│           └── dump.rdb
├── docker-compose.yaml
└── logs
    └── fastapi_tm_celery
        └── x.log

```
