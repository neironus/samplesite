from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb

# Create your views here.

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    content = {'bbs': bbs}
    return HttpResponse(template.render(content, request))