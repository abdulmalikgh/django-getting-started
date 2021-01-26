from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, 'home.html', {})

def about_view(request,*args, **kwargs):
    my_context = {
        'name' : 'Abdul-Malik Musah',
        'about' : 'I am a front end developer with passion for code ',
         'is_alert': True,
         'projects' : ['boma', 'afcfta', 'tribeid']
    }
    return render(request, 'about.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})