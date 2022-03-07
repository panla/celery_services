import threading
from typing import Union
from datetime import timedelta

from redis.client import Redis
from redis.connection import ConnectionPool

from config import RedisConfig

REDIS_CONNECTION_PARAMS = {
    'max_connections': RedisConfig.MAX_CONNECTIONS,
    'username': RedisConfig.USER,
    'password': RedisConfig.PASSWD,
    'host': RedisConfig.HOST,
    'port': RedisConfig.PORT,
    'encoding': 'utf-8',
    'decode_responses': True
}


class Pool:
    cache = dict()
    lock = threading.Lock()
    instance = None

    def __init__(self, db: int = 0) -> None:
        self.db = db

    def __new__(cls, db: int = 0):
        db = str(db)

        with cls.lock:
            if not cls.instance:
                cls.instance = super().__new__(cls)

            if not cls.cache.get(db):
                cls.cache[db] = ConnectionPool(db=db, **REDIS_CONNECTION_PARAMS)

            return cls.instance

    def pool(self):
        return self.cache.get(str(self.db))


class BaseRedis(object):
    DB = 0
    PREFIX_KEY = ''

    def __init__(self) -> None:
        self._name = None
        self.client: Redis = Redis(connection_pool=Pool(self.DB).pool())

    @property
    def name(self):
        return self._name

    @name.setter
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

    def get_values(self, keys):
        return self.client.hmget(name=self.name, keys=keys)

    def expire(self, seconds):
        return self.client.expire(name=self.name, time=seconds)

    def delete(self):
        return self.client.delete(self.name)

    def exists(self) -> bool:
        return bool(self.client.exists(self.name))
