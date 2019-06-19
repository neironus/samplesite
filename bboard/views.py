from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb, Rubric

# Create your views here.

def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(requset, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(requset, 'bboard/by_rubric.html', context)