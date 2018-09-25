# -*- coding: utf-8 -*-

# get twitter API form tweepy
import tweepy 
import wget


# use your own token to authorize the function of the API
consumer_key = "your API key"
consumer_secret = "your API secret key"
access_key = "your access token"
access_secret = "your access token secret"


# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


#this  funtion download tweets from tweet
def get_tweet(image_name):
    
    image = []    
    new_tweets = api.user_timeline(screen_name='football',
                                   count=10, include_rts=False,
                                   exclude_replies=True)
    
    image.extend(new_tweets)
    
    
    image_files = []
    for item in new_tweets:
        image = item.entities.get('media', [])
        image_files.append(image[item]['media_url'])
            
            
    error_count = 0
    for each_image_file in image_files:
        if each_image_file.endswith(".jpg"):
            wget.download(each_image_file)
        else:
            print("Sorry, but there is no image here!")
            error_count += 1
    
    print("There exists: " , error_count, "errors!")
    


    
   