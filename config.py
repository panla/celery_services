__all__ = [
    'BASE_DIR',
    'Config',
    'LogConfig',
    'RedisConfig',
    'MQConfig'
]

import os
from pathlib import Path
from functools import lru_cache

import pytomlpp
from pydantic import BaseModel

from conf.settings import (
    LogSetting, RedisSetting, MQSetting
)

BASE_DIR = Path(__file__).absolute().parent


class Setting(BaseModel):
    log: LogSetting
    redis: RedisSetting
    mq: MQSetting


@lru_cache()
def get_settings() -> Setting:
    code_env = os.environ.get('CODE_ENV', 'prd')

    if code_env == 'test':
        p = Path(BASE_DIR).joinpath('conf/test.local.toml')
    else:
        p = Path(BASE_DIR).joinpath('conf/product.local.toml')

    if not p.is_file():
        raise Exception('config no exists')

    settings = Setting.parse_obj(pytomlpp.load(p))
    return settings


Config = get_settings()

LogConfig = Config.log
RedisConfig = Config.redis
MQConfig = Config.mq
