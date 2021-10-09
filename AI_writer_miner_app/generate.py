from gnews import GNews
google_news = GNews()
from english_words import english_words_set
english_words_list = list(english_words_set)
import random
from newspaper import Article
def get_text(key = None):
    key = key or random.choice(english_words_list)
    while 1:
        newss = google_news.get_news(key)
        if len(newss): break
        print(f"not enough news from keyword {key}")
        key = random.choice(english_words_list)
    news = random.choice(newss)
    article = Article(eval(news.__str__())['url'])
    article.download()
    article.parse()
    return article.text
