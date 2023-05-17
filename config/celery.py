from __future__ import absolute_import, unicode_literals

import os
import django

from celery import Celery


os.environ['DJANGO_SETTINGS_MODULE'] = 'whisper.settings'
django.setup()


app = Celery("config")
app.conf.enable_utc = False
app.conf.update(timezone="Africa/Lagos")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
