from loguru import logger
from extensions.task import BaseTask
from services.application import app


@app.task(bind=True, base=BaseTask, name='pay')
def pay(self, payload: dict):
    """Pay Task"""

    logger.info('Get One Task')
    # logger.info(type(self.request))
    # celery.app.task.Context
