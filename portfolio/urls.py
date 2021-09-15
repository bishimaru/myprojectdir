from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [

    path('', views.index, name='portfolio'),
    path('airbnb1', views.airbnb1index, name='airbnb1'),
    path('airbnb2', views.airbnb2index, name='airbnb2'),


]
