# -*- encoding: utf-8 -*-
import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

class TwitterClient():
    __oauth = None

    def __init__(self, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                    auth_token=OAUTH_TOKEN, auth_token_secret=OAUTH_TOKEN_SECRET):
        self.__consumer_key = consumer_key      
        self.__client_secret = consumer_secret
        self.__auth_token = auth_token
        self.__auth_token_secret = auth_token_secret


    def get_last_200_followers(self, screen_name):
        url_path = 'followers/list.json'
        params = {'screen_name': screen_name, 'count':'200'}
        return self.__get_query_with_params(url_path, params)


    def get_last_200_tweets(self, screen_name):
        url_path = 'statuses/user_timeline.json'
        params = {
            'screen_name': screen_name,
            'count': '200',
            'exclude_replies': 'false',
            'include_rts': 'true'
        }
        return self.__get_query_with_params(url_path, params)


    def __get_query_with_params(self, url_path, params):
        self.__oauth = OAuth1(self.__consumer_key,
                client_secret=self.__client_secret,
                resource_owner_key=self.__auth_token,
                resource_owner_secret=self.__auth_token_secret)
        r = requests.get(
            url = "https://api.twitter.com/1.1/%s" % url_path,
            params=params,
            auth = self.__oauth
        )
        return r.json()


    def __get_query(self, url_path):
        self.__oauth = OAuth1(self.__consumer_key,
                client_secret=self.__cient_secret,
                resource_owner_key=self.__auth_token,
                resource_owner_secret=self.__auth_token_secret)
        r = requests.get(
            url = "https://api.twitter.com/1.1/%s" % url_path,
            auth = self.__oauth
        )
        return r.json()