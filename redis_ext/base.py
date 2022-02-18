from typing import Union
from datetime import timedelta

from redis import Redis

from config import RedisConfig


class BaseRedisClient(object):
    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self) -> None:
        self._name = None
        self.uri = 'redis://{}:{}@{}:{}/{}'.format(
            RedisConfig.USER, RedisConfig.PASSWD, RedisConfig.HOST, RedisConfig.PORT, self.DB
        )
        self.client: Redis = Redis.from_url(self.uri, **self.CONNECTION_PARAMS)

    @property
    def name(self):
        return self._name

    @property
    def name(self, value):
        self._name = f'{self.PREFIX_KEY}:{value}'

    def get(self):
        return self.client.get(name=self.name)

    def set(self, value, ex: Union[int, timedelta] = None, px: Union[int, timedelta] = None):
        return self.client.set(name=self.name, value=value, ex=ex, px=px)

    def set_nx(self, value):
        return self.client.setnx(name=self.name, value=value)

    def getset(self, value):
        return self.client.getset(name=self.name, value=value)

    def set_kv(self, key, value):
        return self.client.hset(name=self.name, key=key, value=value)

    def get_kv(self, key):
        return self.client.hget(name=self.name, key=key)

    def set_mapping(self, mapping: dict):
        return self.client.hmset(name=self.name, mapping=mapping)

    def get_all_values(self):
        return self.client.hgetall(name=self.name)

    def expire(self, seconds):
        return self.client.expire(name=self.name, time=seconds)

    def delete(self):
        return self.client.delete(self.name)

    def exists(self):
        return self.client.exists(self.name)
