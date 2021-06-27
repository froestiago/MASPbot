import pandas as pd
import numpy as np
from numpy import random
import tweepy
import requests
import os
from time import time, sleep

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

def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200: #200 means we got it
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk) #save the image

        api.update_with_media(filename, status=message) #TWEET
        os.remove(filename)        #deletes the image
    else:
        print("Unable to download image")

def get_random_post(data):
    x = random.randint(len(data))
    print(x) #print the art work index
    post = data.iloc[x] #get the art work from the dataset
    data.at[x, 'posted'] = 1    # 1 means it has been posted
    text = post['artist'] + '. ' + post['title & year'] + ' ' + post['website url'] #mount the tweet
    img_url = post['image url']
    posted = post['posted']
    return text, img_url, posted, data

####################################
# # # # # # #   MAIN   # # # # # # #
####################################

data = pd.read_csv('data.csv') 

four_hours = 4*60*60 #seconds

api = twitter_api()
while True:
    print('Got it!')
    sleep(four_hours - time() % four_hours) #wait
    tweet, url, check, data = get_random_post(data) #get data
    if(check==1.0): #check if it has been already posted
        while(check == 1.0): #i.e if already posted get another
            print("already posted")
            tweet, url, check, data = get_random_post(data)
            print(tweet)
            print(url)
    else:
        print(tweet)
        print(url)

    tweet_image(url, tweet) #TWEET  
    data.to_csv('data.csv') #save new file with posted updated
    
    print('Done!')