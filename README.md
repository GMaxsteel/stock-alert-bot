# 📈 Stock Market News Alert Bot

This bot tracks news about Indian stock markets and companies using specific keywords. It monitors:
- 🗞 RSS feeds (like Moneycontrol, ET)
- 🐦 Twitter (via API)
- 🔺 Reddit (Indian stock market subreddits)

Whenever it finds a match, it sends you a 📲 Telegram alert.

---

## ✅ Features

- Keyword-based tracking
- Telegram alerts
- Twitter + Reddit integration
- Easy to set up (just fill in your keys)
- Run locally or host on cloud

---

## 🚀 Setup Guide

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/stock-alert-bot.git
cd stock-alert-bot
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Fill your API keys

Edit `bot_config.py` with:

- `TELEGRAM_TOKEN`: from [@BotFather](https://t.me/botfather)
- `TELEGRAM_CHAT_ID`: from [@userinfobot](https://t.me/userinfobot)
- `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`: [Reddit Apps](https://www.reddit.com/prefs/apps)
- `TWITTER_BEARER_TOKEN`: from [Twitter Developer Portal](https://developer.twitter.com/)

### 4. Run the bot

```bash
python scheduler.py
```

---

## 🧠 How It Works

1. `news_alerts.py`: Parses RSS feeds and finds keyword matches.
2. `reddit_alerts.py`: Uses Reddit API to find matching posts.
3. `twitter_alerts.py`: Searches recent tweets via Twitter API.
4. `scheduler.py`: Runs all 3 modules every 15 minutes.

---

## 🛠 Hosting (Optional)

To run this 24/7, deploy on:
- [Railway](https://railway.app)
- [Render](https://render.com)
- [PythonAnywhere](https://pythonanywhere.com)

Or use `cron`/Task Scheduler on your system.

---

## 💬 Credits & License

Built by [Akshay Malhotra](https://github.com/yourgithub). MIT License.
