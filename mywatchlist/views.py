from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from mywatchlist.models import MyWatchlist

def show_html(request):
    data= MyWatchlist.objects.all()
    context = {"data": data}
    return render(request, "watchlist.html", context)


def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json",)


def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml",)