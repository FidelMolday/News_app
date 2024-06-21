from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    news_api = NewsApiClient(api_key = '17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsApi.get_top_headlines(sources='bbc-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = article[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request,"main/index.html", context={"mylist": mylist})    