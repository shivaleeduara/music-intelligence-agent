import feedparser

RSS_FEEDS = {
    "Pitchfork": "https://pitchfork.com/rss/news/",
    "Rolling Stone": "https://www.rollingstone.com/music/music-news/feed/",
    "Billboard": "https://www.billboard.com/feed/"
}

def get_latest_articles():

    articles = []

    for source, url in RSS_FEEDS.items():

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            articles.append({
                "source": source,
                "title": entry.title,
                "link": entry.link
            })

    return articles