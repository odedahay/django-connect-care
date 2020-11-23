from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        
        # If no attachedment, MultiValueDictKeyError error, how do I deal with it
        if 'cv_document' in request.FILES:
            cv_file = request.FILES['cv_document']
        else:
            cv_file = False

        messages = request.POST.get('messages')

        # save to DB
        contact = Contact(name=name, email=email, phone=phone, cv_file=cv_file, message=messages)
        contact.save()

        # attached file
        #email.content_subtype = 'html'

        # send_mail will not work if email has attached file
        # send_mail(
        #     'Message from ' + name,
        #     message,
        #     'odedahay@gmail.com',
        #     ['odedahay@yahoo.com'],
        #     fail_silently=False,
        # )
        try:
            #settings.EMAIL_HOST_USER,
            mail = EmailMessage(
                'Message from ' + name, 
                'Contact Number: ' +  phone + '\n\n' + messages + '\n\n' + 'Sign into the admin panel for more info', 
                'inquiry@connectandcareph.com', 
                ['media@cnc-international.com'], # recipient email change to --> media@cnc-international.com
                reply_to=[email]
            )

            if 'cv_document' in request.FILES:
                mail.attach(cv_file.name, cv_file.read(), cv_file.content_type)
        
            mail.send(fail_silently=False)
        
        except BadHeaderError:
            return HttpResponse('Invalid header found')

        return redirect('/contacts/thank-you')

    return render(request, 'contacts/contact_forms.html')


def thank_you(request):
    return render(request, 'contacts/thank_you.html')
