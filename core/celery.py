import os

from celery import Celery
from celery.schedules import crontab

from coins.tasks import task_update_price


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery beat
@app.on_after_configure.connect
def update_coin_price(sender, **kwargs):
    sender.add_periodic_task(10.0, task_update_price.s(), name='scrape_coin_price')
