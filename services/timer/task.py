import time
from datetime import datetime

from extensions import logger
from services.application import app


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10, timer_task.s(), name='timer task')


def test33():
    time.sleep(3)
    print('test33')


def test44():
    time.sleep(4)
    print('test44')
    test33()


@app.task
def timer_task():
    """Timer Task

    TODO USE right logger
    """

    logger.info(datetime.now())

    test33()
    test44()

    return 'success'
