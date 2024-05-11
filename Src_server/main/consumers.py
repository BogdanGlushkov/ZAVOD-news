from channels.generic.websocket import AsyncWebsocketConsumer
import json

from django.shortcuts import get_object_or_404

from .models import News


class ReviewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'review'

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        theme_slug = text_data_json['theme_slug']
        theme = News.objects.get(slug=theme_slug)
        if text_data_json['action']:
            action = text_data_json['action']

            if action == 'like':
                theme.likes += 1
            if action == '-like':
                theme.likes -= 1
            if action == 'dislike':
                theme.dislikes += 1
            if action == '-dislike':
                theme.dislikes -= 1

            theme.save()

        event = {
            'type': 'send_message',
            'likes': theme.likes,
            'dislikes': theme.dislikes
        }

        await self.channel_layer.group_send(self.group_name, event)

    async def send_message(self, event):

        likes = event['likes']
        dislikes = event['dislikes']

        await self.send(text_data=json.dumps({
            'likes': likes,
            'dislikes': dislikes,
        }))
