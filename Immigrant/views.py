from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Culture, Region, Event
import json
import re

# Create your views here.
def au_display(request):
    context = {}
    return render(request, "au_info.html", context)

def cn_display(request):
    data = Region.objects.all()
    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    year2021 = {'time': 2021}
    for item in data:
        name = str(item.country_name)
        if name == 'China':
            if int(item.year) == 1996:
                year1996[name] = item.migrant_num
            if int(item.year) == 2001:
                year2001[name] = item.migrant_num
            if int(item.year) == 2006:
                year2006[name] = item.migrant_num
            if int(item.year) == 2011:
                year2011[name] = item.migrant_num
            if int(item.year) == 2016:
                year2016[name] = item.migrant_num
            if int(item.year) == 2021:
                year2021[name] = item.migrant_num
    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016, 2021: year2021}
    return render(request, "cn_info.html", {'cn_trends': json.dumps(dic)})

def nz_display(request):
    data = Region.objects.all()
    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    year2021 = {'time': 2021}
    for item in data:
        name = str(item.country_name)
        if name == 'New Zealand':
            if int(item.year) == 1996:
                year1996[name] = item.migrant_num
            if int(item.year) == 2001:
                year2001[name] = item.migrant_num
            if int(item.year) == 2006:
                year2006[name] = item.migrant_num
            if int(item.year) == 2011:
                year2011[name] = item.migrant_num
            if int(item.year) == 2016:
                year2016[name] = item.migrant_num
            if int(item.year) == 2021:
                year2021[name] = item.migrant_num
    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016, 2021: year2021}
    return render(request, "nz_info.html", {'nz_trends': json.dumps(dic)})

def uk_display(request):
    data = Region.objects.all()
    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    year2021 = {'time': 2021}
    for item in data:
        name = str(item.country_name)
        if name == 'United Kingdom':
            if int(item.year) == 1996:
                year1996[name] = item.migrant_num
            if int(item.year) == 2001:
                year2001[name] = item.migrant_num
            if int(item.year) == 2006:
                year2006[name] = item.migrant_num
            if int(item.year) == 2011:
                year2011[name] = item.migrant_num
            if int(item.year) == 2016:
                year2016[name] = item.migrant_num
            if int(item.year) == 2021:
                year2021[name] = item.migrant_num
    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016, 2021: year2021}
    return render(request, "uk_info.html", {'uk_trends': json.dumps(dic)})

def india_display(request):
    data = Region.objects.all()
    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    year2021 = {'time': 2021}
    for item in data:
        name = str(item.country_name)
        if name == 'India':
            if int(item.year) == 1996:
                year1996[name] = item.migrant_num
            if int(item.year) == 2001:
                year2001[name] = item.migrant_num
            if int(item.year) == 2006:
                year2006[name] = item.migrant_num
            if int(item.year) == 2011:
                year2011[name] = item.migrant_num
            if int(item.year) == 2016:
                year2016[name] = item.migrant_num
            if int(item.year) == 2021:
                year2021[name] = item.migrant_num
    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016, 2021: year2021}
    return render(request, "india_info.html", {'india_trends': json.dumps(dic)})

def vn_display(request):
    data = Region.objects.all()
    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    year2021 = {'time': 2021}
    for item in data:
        name = str(item.country_name)
        if name == 'Vietnam':
            if int(item.year) == 1996:
                year1996[name] = item.migrant_num
            if int(item.year) == 2001:
                year2001[name] = item.migrant_num
            if int(item.year) == 2006:
                year2006[name] = item.migrant_num
            if int(item.year) == 2011:
                year2011[name] = item.migrant_num
            if int(item.year) == 2016:
                year2016[name] = item.migrant_num
            if int(item.year) == 2021:
                year2021[name] = item.migrant_num
    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016, 2021: year2021}
    return render(request, "vn_info.html", {'vn_trends': json.dumps(dic)})

def event_display(request):
    events = Event.objects.all()
    paginator = Paginator(events, 5)
    page_num = request.GET.get('page', 1)
    page_of_events = paginator.get_page(page_num)

    context = {}
    context['page_of_events'] = page_of_events
    return render(request, "event_display.html", context)

def search(request):
    keyword = request.GET.get('keyword', '')
    year = request.GET.get('year', '')
    month = request.GET.get('box-month', '')
    day = request.GET.get('box-day', '')
    if month != '':
        startdate = year + '-' + month + '-' + day
    else:
        if year != '':
            startdate = year
        else:
            startdate = ''
    if startdate == '' and keyword == '':
        search_events = Event.objects.all()
    elif startdate == '' and keyword != '':
        search_events = Event.objects.filter(title__icontains=keyword)
    else:
        search_events = Event.objects.filter(title__icontains=keyword, start_date__contains=startdate)

    paginator = Paginator(search_events, 5)
    page_num = request.GET.get('page', 1)
    page_of_events = paginator.get_page(page_num)

    context = {}
    context['search_keyword'] = keyword
    context['search_startdate'] = startdate
    context['page_of_events'] = page_of_events
    context['search_events_count'] = search_events.count()
    return render(request, 'event_search.html', context)


def map_display(request):
    context = {}
    return render(request, 'mel_map.html', context)

def garden_report(request):
    context = {}
    return render(request, 'garden_report.html', context)

def garden_find(request):
    context = {}
    return render(request, 'garden_find.html', context)

'''
def searchTest(request):
    search_word = request.GET.get('keyword','')
    search_events = Event.objects.filter(title__icontains=search_word)
    context = {}
    context['events'] = search_events
    return render(request, 'event_search.html',context)
'''