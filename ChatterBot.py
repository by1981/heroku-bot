# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "k4RhBKTbWgAr2bxbxnSduEumb"
consumer_secret = "tgab5rK3CB1fB1AB5KtdR234qiHNDTNt6yPZdX2PgYj3F3jY7F"
access_token = "923094259116281858-jEA1OviraMGwl9TAMEUaROpADIiiS9e"
access_token_secret = "ps67oZirPRbnb2eapDIJoaOIIgtxaM3EgFUbGawYjYqvw"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
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
