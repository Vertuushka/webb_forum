import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

class DialogConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = f"dialog_{self.scope['url_route']['kwargs']['id']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text_data_json['time'] = datetime.now().strftime("%d/%m/%Y - %H:%M")
        await self.create_message(data=text_data_json)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',
                'message': text_data_json
            }
        )

    async def send_message(self, event):
        await self.send(text_data=json.dumps({'message': event['message']}))

    @database_sync_to_async
    def create_message(self, data):
        dialog_id = int(data['dialog_id'])
        sender_id = int(data['sender'])
        receiver_id = int(data['receiver'])
        dialog = Dialog.objects.get(id=dialog_id)
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        new_message = Private_Message(
            dialog=dialog,
            sender=sender,
            receiver=receiver,
            content=data['message'],
            time_created=datetime.strptime(data['time'], "%d/%m/%Y - %H:%M")
        )
        new_message.save()