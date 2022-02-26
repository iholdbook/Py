import feedparser
NewsFeed = feedparser.parse("https://vc.ru/rss")
entry = NewsFeed.entries[0]
print(entry.keys())

import feedparser
NewsFeed = feedparser.parse("https://vc.ru/rss") # http://static.feed.rbc.ru/rbc/logical/footer/news.rss
print('Number of RSS posts :', len(NewsFeed.entries))
entry = NewsFeed.entries[0]
print('Post Title :', entry.title, ' Link: ', entry.link)


import requests
def send_telegram(text: str):
    token = "ТОКЕН" # ТОКЕН
    url = "https://api.telegram.org/bot"
    channel_id = "@КАНАЛ" # @КАНАЛ
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram(entry.title+' '+entry.link) # ПУБЛИКУЕМЫЙ_ТЕКСТ
