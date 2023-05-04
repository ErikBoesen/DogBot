import sys
sys.path.insert(0, 'vendor')

import requests
import json


def receive(event, context):
    message = json.loads(event['body'])

    bot_id = message['bot_id']
    response = process(message)
    if response:
        send(response, bot_id)

    return {
        'statusCode': 200,
        'body': 'ok'
    }


def get_dog_url():
    req = requests.get('https://dog.ceo/api/breeds/image/random')
    return req.json()['message']


def process(message):
    # Prevent self-reply
    if message['sender_type'] != 'bot':
        if 'dog' in message['text'].lower():
            return get_dog_url()


def send(text, bot_id):
    url = 'https://api.groupme.com/v3/bots/post'

    message = {
        'bot_id': bot_id,
        'text': text,
    }
    r = requests.post(url, json=message)
