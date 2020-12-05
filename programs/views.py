from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Program
from pages.models import Page

def index(request):
    program_intro = Page.objects.filter(slug__exact='programs')
    programs = Program.objects.order_by('order_by').filter(is_published=True)

    paginator = Paginator(programs, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
 
    context = {
        'program_intro':program_intro,
        'programs':programs
    }
    return render(request, 'programs/programs.html', context)

def program_detail(request, c_slug=None):

    program_detail = get_object_or_404(Program, slug=c_slug)

    context = {
        'program': program_detail
    }

    return render(request, 'programs/program_detail.html', context)
