from django.shortcuts import render

def contact(request):
    return render(request, 'contact/base_contact.html')

# Create your views here.
