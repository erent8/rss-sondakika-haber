import feedparser

# CNN Türk Spor RSS feed URL'si
rss_url = 'https://www.cnnturk.com/feed/rss/ekonomi/news'

# RSS verisini çek
feed = feedparser.parse(rss_url)

# RSS başlıkları, açıklamalar ve yayın tarihleri
for entry in feed.entries:
    print(f"Başlık: {entry.title}")
    print(f"Açıklama: {entry.description}")
    print(f"Yayınlanma Tarihi: {entry.published}")
    print("-" * 50)
