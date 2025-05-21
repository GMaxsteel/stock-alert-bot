import praw
from bot_config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, KEYWORDS
from news_alerts import send_telegram_alert

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def check_reddit():
    for submission in reddit.subreddit("IndianStockMarket+StockMarketIndia").new(limit=15):
        for kw in KEYWORDS:
            if kw.lower() in submission.title.lower():
                send_telegram_alert("Reddit: " + submission.title, submission.url)