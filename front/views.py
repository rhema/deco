from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from deco.front.models import *

def home(request):
    #sections = Section.objects.all().order_by('sortnum')
    urls = " "
    for item in Item.objects.all():
        urls += " <a href=\""+item.url()+"\">"+item.url()+"</a>"
    return HttpResponse("list of urls:"+urls)#render_to_response('index.html', {"sections": sections})

def item_page(request,item):
    #sections = Section.objects.all().order_by('sortnum')
    #return HttpResponse("item "+item)#render_to_response('index.html', {"sections": sections})
    db_item = Item.objects.get(title=item.replace('_',' '))
    return render_to_response('item.html', {'title': db_item.title,'rendered': db_item.render()})

def tage_page(request):
    #sections = Section.objects.all().order_by('sortnum')
    return HttpResponse("tag")#render_to_response('index.html', {"sections": sections})