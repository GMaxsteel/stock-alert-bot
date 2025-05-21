import time
from news_alerts import check_news
from reddit_alerts import check_reddit
from twitter_alerts import check_twitter

while True:
    check_news()
    check_reddit()
    check_twitter()
    time.sleep(900)  # Run every 15 minutes