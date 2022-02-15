from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import request
import requests
from bs4 import BeautifulSoup as bsoup
from newspaper import Article
import nltk.data
# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def rscrape(request):
    url = requests.get('https://rss.nytimes.com/services/xml/rss/nyt/World.xml')
    soup = bsoup(url.content, "xml.parser")
    items = bsoup.find_all('item')
    
    for item in items:
        article_title = items.title.text
        article_summary = items.description.text
        article_link = items.link['href']
        print(f"Title: {article_title}\n\nSummary: {article_summary}\n\nLink: {article_link}")

def summ_article(url):
    article = Article(url)
    
    article.download()
    article.parse()
    
    article.download('punkt')
    article.nlp()
    date = article.publish_date
    date = str(date.strftime("%m/%d/%Y"))
    article_img = str(article.top_image)
    print(f"Author: {article.authors}\n")
    print(f"Publish Date: {date}\n")
    print(f"Top Image Url: {article_img}\n")
summ_article("https://www.nytimes.com/2022/02/08/business/energy-environment/electric-cars-vehicles.html")   
    