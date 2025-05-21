import feedparser, requests
from bot_config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, KEYWORDS, FEEDS

def send_telegram_alert(title, link):
    msg = f"📢 *{title}*\n{link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def check_news():
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            for kw in KEYWORDS:
                if kw.lower() in entry.title.lower() or kw.lower() in entry.summary.lower():
                    send_telegram_alert(entry.title, entry.link)