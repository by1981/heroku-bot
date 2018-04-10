# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "bKTlaC8L7zYVfowESkdtt8rP3"
consumer_secret = "gdOTuyrDZuy5NkoEo5tNwcw0EOQDTV1ruIsC9xlWRtO25PI9z4"
access_token = "983584039410937856-nnjmotaJ3LS9b167WoR9fAVgKSRbpqf"
access_token_secret = "EF67djB5DwoAZ9Q5w8eTSTqeUZUOQBfuzSXlMgnnwcvfS"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop!! Won't stop!! Chatting! This is Tweet #%s!" %
        tweet_number)

# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

# New comment