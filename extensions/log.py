__all__ = ['logger']

import sys
from pathlib import Path

from loguru import logger

from config import LogConfig

Path(LogConfig.PATH).parent.mkdir(exist_ok=True)
level = LogConfig.LEVEL.upper()

logger.remove()
logger.add(
    LogConfig.PATH, level=level, rotation=LogConfig.ROTATION, retention=LogConfig.RETENTION, backtrace=True,
    diagnose=True, enqueue=True, compression=LogConfig.COMPRESSION
)
if LogConfig.STDOUT:
    logger.add(sys.stdout, level=level, backtrace=True, diagnose=True, enqueue=True)
