from django.urls import path
from . import views

app_name = 'esearch'
urlpatterns = [path('', views.search_index)]