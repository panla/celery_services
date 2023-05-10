import threading
from typing import Union, Optional
from datetime import timedelta

from redis.client import Redis
from redis.connection import ConnectionPool

from config import RedisConfig
from common import singleton

REDIS_CONNECTION_PARAMS = {
    'max_connections': RedisConfig.MAX_CONNECTIONS,
    'username': RedisConfig.USER,
    'password': RedisConfig.PASSWD,
    'host': RedisConfig.HOST,
    'port': RedisConfig.PORT,
    'encoding': 'utf-8',
    'decode_responses': True
}


@singleton
class Pool:
    def __init__(self, db: int = 0) -> None:
        self.db = ConnectionPool(db=db, **REDIS_CONNECTION_PARAMS)

    def pool(self):
        return self.db


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

    def expire(self, seconds):
        return self.client.expire(name=self.name, time=seconds)

    def delete(self):
        return self.client.delete(self.name)

    def exists(self) -> bool:
        return bool(self.client.exists(self.name))

    def get(self):
        return self.client.get(name=self.name)

    def set(
            self,
            value,
            ex: Union[int, timedelta] = None,
            px: Union[int, timedelta] = None,
            nx: bool = False,
            xx: bool = False,
            get: bool = False
    ):
        """Set the value at key ``name`` to ``value``

        ``ex`` sets an expired flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expired flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)
        """

        return self.client.set(name=self.name, value=value, ex=ex, px=px, nx=nx, xx=xx, get=get)

    def set_nx(self, value):
        return self.client.setnx(name=self.name, value=value)

    def hash_set(self, key: Optional[str] = None, value: Optional[str] = None, mapping: Optional[dict] = None):
        return self.client.hset(name=self.name, key=key, value=value, mapping=mapping)

    def hash_get(self, key):
        return self.client.hget(name=self.name, key=key)

    def hash_get_all_values(self):
        return self.client.hgetall(name=self.name)

    def hash_get_values(self, keys):
        return self.client.hmget(name=self.name, keys=keys)
