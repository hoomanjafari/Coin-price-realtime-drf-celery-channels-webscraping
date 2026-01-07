from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from .scraper import scrape




@shared_task
def task_update_price():
    data = scrape()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'coins_live_price',
        {
            'type': 'send_update',
            'data': {
                'data': data,
                'message': 'success',
            }
        }
    )
