from celery import Celery
from celery.schedules import crontab
import os
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship.settings')

app = Celery('internship')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    # Executes every hour.
    'collect-news-every-hour': { 
         'task': 'databases.task.demo_program', 
         'schedule':  60.0,
        },          
}

# CELERY_BEAT_SCHEDULE = {
#     # Executes every hour.
#     'collect-news-every-hour': { 
#          'task': 'databases.task.demo_program', 
#          'schedule':  60.0,
#         },          
# }
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
