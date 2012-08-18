from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from deco.front.models import *

def home(request):
    #sections = Section.objects.all().order_by('sortnum')
    return HttpResponse("hello world")#render_to_response('index.html', {"sections": sections})