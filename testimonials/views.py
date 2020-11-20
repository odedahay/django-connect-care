from django.shortcuts import render
from .models import Testimonial

def index(request):
    testimonial = Testimonial.objects.order_by('-created_date').filter(is_published=True)
   
    context = {
        'testimonial':testimonial
    }
    return render(request, 'testimonials/testimonials.html', context)
