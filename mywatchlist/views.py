from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchList

def show_my_watch_list(request):
    watch_list_data = WatchList.objects.all()
    context = {
        'watch_list': watch_list_data,
        'nama': 'Gabriel Zebaoth Krisopras Putra',
        'student_id' : '2106751480',
    }

    return render(request, "my_watch_list.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")