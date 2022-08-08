from django.shortcuts import render
from .models import Message
from django.http import JsonResponse


def contact_us(request):
    context = {'section': 'contact_us'}
    return render(request, 'contact-us.html', context)


def get_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('emailAddress')
        message = request.POST.get('message')
        if message != '':
            Message.objects.create(
                name=name,
                email=email,
                message=message
            )
    return JsonResponse({'status': 'Success'})
