from celery import Celery

from django.conf import settings


app = Celery('config')
app.conf.update(
    enable_utc=False,
    result_expires=3600,
    timezone=settings.TIME_ZONE

)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
