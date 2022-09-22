from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchList
def show_home(request):
    return render(request, "mywatchlist_home.html")

def show_html(request):
    watch_list_data = WatchList.objects.all()
    count_watched_film = WatchList.objects.filter(watched=True).count()
    count_unwatched_film = WatchList.objects.filter(watched=False).count()
    is_watched_greater_than_unwatched = count_watched_film >= count_unwatched_film
    context = {
        'boolean_check': is_watched_greater_than_unwatched,
        'watch_list': watch_list_data,
        'nama': 'Gabriel Zebaoth Krisopras Putra',
        'student_id' : '2106751480',
    }

    return render(request, "my_watch_list.html", context)


def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")