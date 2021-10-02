from django.core.checks import messages
from django.core.management.base import BaseCommand
import tweepy
from django.db.models import Max
from twttrbot.models import InboundDirectMessage
from twttrbot.utils import get_auth_api
import datetime as dt

def convert_timestamp_to_date(ts):
    ts = int(str(ts).split('.')[0]) / 1000
    return dt.datetime.fromtimestamp(ts)

def convert_date_to_timestamp(date_obj):
    return int(date_obj.timestamp() * 1000)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        try:

            last_timestamp = InboundDirectMessage.objects.aggregate(Max('sent_on'))

            if last_timestamp:
                last_timestamp = last_timestamp.get('sent_on_max')

            obj_list = list()
            api = get_auth_api()

            receiver_id = str(api.me().id)

            for message in tweepy.Cursor(api.list_direct_messages).items():

                if message.message_create['target']['recipient_id'] == receiver_id:

                    sent_on = convert_timestamp_to_date(message.created_timestamp)

                    if last_timestamp is None or (last_timestamp is not None and sent_on > last_timestamp):
                        sender = api.get_user(str(message.message_create['sender_id'])).screen_name
                        msg = message.message_create['message_data']['text']

                        obj_list.append(InboundDirectMessage(sender=sender, message=msg, sent_on=sent_on))
                    else:
                        break
            InboundDirectMessage.objects.bulk_create(obj_list)
        
        except Exception as e:
            print(e)