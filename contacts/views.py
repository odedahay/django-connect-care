from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import base64

from django.conf import settings
import os

from django.core.mail import EmailMessage

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        messages = request.POST.get('messages')
        
        # If no attachment, MultiValueDictKeyError error, how do I deal with it
        if 'cv_document' in request.FILES:
            cv_file = request.FILES['cv_document']
        else:
            cv_file = False

        # Save to DB
        contact = Contact(name=name, email=email, phone=phone, cv_file=cv_file, message=messages)
        contact.save()

        # send_mail will not work if email has attached file
        #mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])

        try:
            #settings.EMAIL_HOST_USER,
            mail = EmailMessage(
                'Message from ' + name, 
                'Contact Number: ' +  phone + '\n\n' + messages + '\n', 
                'inquiry@connectandcareph.com',
                ['media@cnc-international.com'], # media@cnc-international.com
                reply_to=[email]              
            )
            #filename = os.path.join(settings.MEDIA_ROOT + '/', contact.cv_file.name)
            mail.content_subtype = 'html'

            if 'cv_document' in request.FILES:
                mail.attach(cv_file.name, contact.cv_file.read(), cv_file.content_type)
            
            mail.send(fail_silently=False)
        
        except BadHeaderError:
            return HttpResponse('Invalid header found')

        return redirect('/contacts/thank-you')

    return render(request, 'contacts/contact_forms.html')


def thank_you(request):
    return render(request, 'contacts/thank_you.html')
