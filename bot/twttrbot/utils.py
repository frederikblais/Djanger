import tweepy
from django.conf import settings

def get_auth_api():
    api_key = settings.API_KEY
    api_secret_key = settings.API_KEY_SECRET
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_TOKEN_SECRET

    authentication = tweepy.OAuthHandler(api_key, api_secret_key)
    authentication.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api