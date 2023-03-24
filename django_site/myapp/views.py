# from django.shortcuts import render
from django.http import HttpResponse

def current_datetime(request):
    html = "<html><body>Шпашибо %s</body></html>" % 'Никита'
    return HttpResponse(html)
