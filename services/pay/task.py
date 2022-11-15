from extensions import logger, BaseTask
from services.application import app
from .logics.pay import PayOperator


@app.task(bind=True, base=BaseTask, name='pay')
def pay(self, payload: dict):
    """Pay Task"""

    PayOperator(payload).pay()
