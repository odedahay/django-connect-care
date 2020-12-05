from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from news.models import News
from testimonials.models import Testimonial
from programs.models import Program

def index(request):
    programs_home = Page.objects.filter(slug__exact='programs-we-offer')
    programs_level = Program.objects.order_by('order_by').filter(is_published=True)[:4]
    section_a = Page.objects.filter(slug__exact='how-can-cc-help-you')
    section_b = Page.objects.filter(slug__exact='why-choose-cc-international')
    latest_testimonials = Testimonial.objects.order_by('-created_date').filter(is_published=True)[:3]
    latest_news = News.objects.order_by('-pub_date').filter(is_published=True)[:2]


    context = {
        'programs_home': programs_home,
        'programs_level':programs_level,
        'section_a':section_a,
        'section_b':section_b,
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
