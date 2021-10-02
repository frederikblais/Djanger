from tweepy import api
from tweepy.streaming import StreamListener
from twttrbot.models import TweetLookUpBadWord, TweetLookUpWord, TweetLookUpCoordinates
from django.core.management.base import BaseCommand
from twttrbot.utils import get_auth_api
import tweepy

class MyStreamListner(tweepy.StreamListener):

    def __init__(self):

        self.bad_words = list(TweetLookUpBadWord.objects.values_list('keyword', flat = True))

        super(MyStreamListner, self).__init__()

    def on_connect(self):
        print('Connected to Twitter API.')
    
    def on_status(self, status):
        tweet_id = status.id
        
        if status.truncated:
            tweet_text = status.extended_tweet['full_text']
        else:
            tweet_text = status.text

        if not hasattr(status, 'retweeted_status'):
            for bad_words in self.bad_words:
                if bad_words in tweet_text:
                    break
            else:
                api = get_auth_api()
                resp = api.create_favorite(tweet_id)
                print('Liked tweet: ',tweet_id)

    def on_error(self, status_code):
        if status_code == 420:
            return False


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            filter_words = TweetLookUpWord.objects.values_list('keyword', flat = True)
            filter_words = ', '.join(filter_words)
            filter_location = TweetLookUpCoordinates.objects.values_list('value', flat = True)
            filter_location = [float(cor) for loc in filter_location for cor in loc.split(',')]
            api = get_auth_api()
            stream_listner = MyStreamListner()
            stream = tweepy.Stream(auth = api.auth, listener = stream_listner, tweet_mode = 'extended')
            stream.filter(track=[filter_words], locations=filter_location)

        except Exception as e:
            print(e)