import tweepy
from bot_config import TWITTER_BEARER_TOKEN, KEYWORDS
from news_alerts import send_telegram_alert

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def check_twitter():
    for kw in KEYWORDS:
        tweets = client.search_recent_tweets(query=kw, max_results=5)
        if tweets.data:
            for tweet in tweets.data:
                send_telegram_alert(f"Twitter: {tweet.text}", f"https://x.com/i/web/status/{tweet.id}")