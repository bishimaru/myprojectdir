from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('store_name', views.StoreNameView.as_view(), name='store_name'),
    path('date', views.DateView.as_view(), name='date'),
    path('detail', views.DetailView.as_view(), name='detail'),
    path('name', views.NameView.as_view(), name='name'),
    path('all_display', views.AllDisplayView.as_view(), name='all_display'),
    path('vue', views.vue, name='vue'),



]
