from django.views.generic.base import TemplateView
import os
from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    template_name = "home.html"
    
    file =  '../Manau - La tribu de Dana (Clip Officiel remasterisé) [80hMEKlLVgQ].ass'
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()

    lyrics = content.split('[Events]')[1]
    lyrics_lines = lyrics.split('Dialogue: ')

    lines = []
    starts = []
    end = []
    for line in lyrics_lines:
        lines.append(",".join(line.split(',')[9:]))
        starts.append(line.split(',')[1])
        end.append(line.split(',')[2])

    starts.pop(0)
    lines.pop(0)
    end.pop(0)

    answer = lines.pop()
    starts.pop()
    end.pop()

    
        
    context = {}
    context["starts"] = starts
    context["end"] = end
    context["lines"] = lines
    return render(request, "nplp/home.html", context=context)