import json
import logging
import math
import time

from channels import Channel
from datetime import datetime, timedelta

from  .models import Timer

LOGGER = logging.getLogger(__name__)


### WebSocket handling ###

def ws_connect(message):
    message.reply_channel.send({'accept': True})
    # Initialise their session
    message.reply_channel.send({'text': "hello"})


# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# This doesn't need @channel_session_user as the next consumer will have that,
# and we preserve message.reply_channel (which that's based on)
def ws_receive(message):
    # All WebSocket frames have either a text or binary payload; we decode the
    # text part here assuming it's JSON.
    # You could easily build up a basic framework that did this encoding/decoding
    # for you as well as handling common errors.
    payload = json.loads(message['text'])
    if payload['command'] == 'status':

        assert 'id' in payload.keys()
        print(payload, "--------------------000000000000000000000000")
        timer_obj = Timer.objects.get(id=int(payload['id']))

        if timer_obj.is_completed:
            status = "completed"
            count = 0
            Channel(message.reply_channel).send({'status': status, count: 0})
        else:
            timer_payload = {'id': payload['id'], 'duration': timer_obj.duration,
                             'reply_channel': message.content['reply_channel']}
            print(timer_payload, '--------------------------------------')
            Channel('timer.start').send(timer_payload)

    print("Received payload : ", payload)


def ws_disconnect(message):
    # Unsubscribe from any connected rooms
    pass


def launch(message):
    print("message received")
    timer_detail = json.loads(message['text'])
    timer_id = int(timer_detail['id'])
    duration = timer_detail['duration']
    reply_channel = message['reply_channel']
    end_time = datetime.now() + timedelta(minutes=int(duration))
    count = int(math.ceil((duration*60)/4))
    timer_obj = Timer.objects.get(id=timer_id)
    timer_obj.started = datetime.now()

    while datetime.now() < end_time:
        print("sleeping for 4 seconds.")
        time.sleep(4)
        count -= 1
        Channel(reply_channel).send({'count': count, 'id': timer_id})
