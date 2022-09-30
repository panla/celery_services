from celery import Celery

from services.config import CeleryConfig

app = Celery('tasks')
app.config_from_object(CeleryConfig)
