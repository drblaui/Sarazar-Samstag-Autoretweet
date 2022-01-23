from warnings import catch_warnings
import tweepy, os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_SECRET"))

api = tweepy.API(auth)

account = "SarazarSamstag"
user = api.get_user(screen_name=account)
tweet = user.timeline()[0]

try:
	tweet.retweet()	
except:
    print("Already retweeted")
try:
	tweet.favorite()
except:
    print("Already favorited")
