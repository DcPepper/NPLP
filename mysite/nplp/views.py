from django.views.generic.base import TemplateView
import os
from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    #file =  '../manau.ass'
    print("AAAAAAAAAAAAAAAAAAAAA")
    musics = [file for file in os.listdir(settings.BASE_DIR / "nplp/static/nplp" ) if file.endswith('.mp3')]
    lyrics = [file for file in os.listdir(settings.BASE_DIR / "nplp/static/nplp" ) if file.endswith('.ass')]
    print(musics)
    print(lyrics)
   
    context = {}
    context['lyrics'] = lyrics
    context['musics'] = musics
    
    return render(request, "nplp/home.html", context=context)