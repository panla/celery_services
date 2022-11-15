import time

from extensions import logger


class PayOperator:

    def __init__(self, payload: dict):
        self.payload = payload

    def pay(self):
        """Pay Task"""

        logger.info('Get One Task')
        logger.info(time.time())
        # logger.info(type(self.request))
        # celery.app.task.Context
