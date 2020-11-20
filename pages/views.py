from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from news.models import News
from testimonials.models import Testimonial

def index(request):

    latest_testimonials = Testimonial.objects.order_by('-created_date').filter(is_published=True)[:3]
    latest_news = News.objects.order_by('-pub_date').filter(is_published=True)[:2]

    context = {
        'latest_news': latest_news,
        'latest_testimonials': latest_testimonials
    }

    return render(request, 'pages/index.html', context)

def about(request):
    about = Page.objects.filter(slug__exact='about')

    context = {
        'about': about
    }
    return render(request, 'pages/about.html', context)

def faq_page(request):
    faq = Page.objects.filter(slug__exact='faq')

    context = {
        'faq': faq
    }
    return render(request, 'pages/faq.html', context)

def contact(request):
    return render(request, 'pages/contact.html')