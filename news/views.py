from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    news_list = News.objects.all()

    context = {
        'news_list':news_list
    }
    return render(request, 'news/news.html', context)

def news_detail(request, c_slug=None):
    
    news_detail = get_object_or_404(News, slug=c_slug)
    news_list = News.objects.all()[:6]
   
    context = {
        'news_detail':news_detail,
        'news_list':news_list
    }
    return render(request, 'news/news_article.html', context)
