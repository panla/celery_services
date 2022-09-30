from datetime import datetime

from celery import Celery

from extensions import BaseTask
from services.config import BeatConfig

beat_app = Celery('BeatTask')
beat_app.config_from_object(BeatConfig)


# FIXME 暂时无法把定时任务分离出去
@beat_app.task(bind=True, base=BaseTask)
def timer_task(self, what):
    print(what)
    print(datetime.now())


@beat_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1.0, timer_task.s('hello'), name='timer_task')
