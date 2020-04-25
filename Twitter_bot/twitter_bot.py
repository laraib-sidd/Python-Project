import tweepy
import time

access_token = None #"Your_acces_token"
access_token_secret = None #"Your_acces_token_secret"
consumer_key = None #"Your_consumer_key"
consumer_secret = None #"your_consumer_secret"

if  not access_token or access_token_secret or consumer_key or consumer_secret :
    print('Get authentication Details')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def generous_bot():
    '''A function to get a list of all
    the followers and follow people as you like.'''

    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(30)

    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == 'moonlight':
            follower.follow()
            break


def like_bot(search_string="python",numberofTweets=2):
    for tweet in tweepy.Cursor(api.search, search_string).items(numberofTweets):
        try:
            tweet.favorite()
            print("I liked that tweet ")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process the status here
    print(status)
    print('\n')
