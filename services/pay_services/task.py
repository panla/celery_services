from loguru import logger
from extensions.task import BaseTask
from services.application import app


@app.task(base=BaseTask, name='pay')
def pay(payload: dict):
    """Pay Task"""

    logger.info('Get One Task')
