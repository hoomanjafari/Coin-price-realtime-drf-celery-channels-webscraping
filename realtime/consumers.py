import random

from channels.generic.websocket import AsyncWebsocketConsumer


class PriceLiveConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        # to include the parent's (AsyncWebsocketConsumer) init
        super().__init__(*args, **kwargs)
        self.sender_name = None
        self.group_name = 'coins_live_price'

    async def connect(self):
        # random_code = self.scope['session']['session_key'][2:6]
        # self.sender_name = f"{random.randint(1000, 9999)}{random_code}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_update(self, event):
        await self.send(text_data=event['data'])



    # async def receive(self, text_data=None, bytes_data=None):
    #     await self.channel_layer.group_send(
    #         self.group_name,
    #         {
    #             'type': 'price_live',
    #             'data': {
    #                 ''
    #             }
    #         }
    #     )
