from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("search",views.search,name='search'),
    path("venue_csv",views.venue_csv,name='venue_csv'),
]
