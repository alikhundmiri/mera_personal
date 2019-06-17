from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab

# # Execute every hour divisible by 1, and every hour during office hours (8am-5pm).
# app.conf.beat_schedule = {
# 	'add-every-minute-contrab': {
# 		'task': 'tasks.tweeting',
# 		'schedule': crontab(minute=13, hour='*/1,9-17'),
# 		'args': (16, 16),
# 	}
# }