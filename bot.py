from numpy import random
import tweepy
import urllib.request
import os
import pickle
import logging

logging.basicConfig(filename = 'log.txt', level=0, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y%I:%M:%S %p')

#use your credentials
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

def twitter_api():  #API stuff, read the reference
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    api = tweepy.API(auth)
    return api

def tweet_image(message, url):
    api = twitter_api()
    f_name = 'temp.jpg'
    try:
        urllib.request.urlretrieve(url, f_name)
        api.update_with_media(f_name, status=message)
        os.remove(f_name)
        logging.debug("Tweet ok")
    except:
        logging.error("Bad request")

def get_random_post():
    with open("MASPbot/data.pickle","rb") as file:
        data = pickle.load(file)
    if len(data):
        i       = random.randint(len(data))
        post    = data.pop(i)
        text    = post['artist'] + '. ' + post['title & year'] + ' ' + post['website url']
        img_url = post['image url']
        with open("MASPbot/data.pickle","wb") as file:
            pickle.dump(data,file)
        return text, img_url, True
    else:
        return None, None, False
    