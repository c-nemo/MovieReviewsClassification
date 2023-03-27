from django.urls import path
from . import views

urlpatterns = [
    # path('', views.current_datetime, name='current_datetime')
    path('', views.index, name="index"),
    path('prediction', views.prediction, name="prediction")
]