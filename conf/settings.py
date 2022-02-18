from typing import Optional

from pydantic import BaseModel


class LogSetting(BaseModel):
    LEVEL: Optional[str] = 'DEBUG'
    PATH: str


class MQSetting(BaseModel):
    """RabbitMQ"""

    HOST: str
    PORT: Optional[int] = 5672
    USER: Optional[str] = 'root'
    PASSWD: Optional[str] = 'root'


class RedisSetting(BaseModel):
    """Redis"""

    HOST: Optional[str] = '127.0.0.1'
    PORT: Optional[int] = 6379
    PASSWD: Optional[str] = ''
    USER: Optional[str] = ''
