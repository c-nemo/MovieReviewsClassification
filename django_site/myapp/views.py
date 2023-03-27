from django.shortcuts import render
from pathlib import Path
# from django.http import HttpResponse
from .apps import MyappConfig

# def current_datetime(request):
#     html = "<html><body>Шпашибо %s</body></html>" % 'Никита'
#     return HttpResponse(html)

def index(request):
    return render(request, "base.html", {"prediction": "None"})

def prediction(request):
    text = request.POST.get('text', 'This movie is disgustingly good!')
    if not text:
        text = 'This movie is disgustingly good!'
    ls = MyappConfig.pipe(text)
    prediction = MyappConfig.get_prediction(ls)
    prediction['text'] = text
    return render(request, "base.html", {"prediction": prediction, "settings": prediction})