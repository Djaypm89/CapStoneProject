
from . import views 
from .views import HousingDataList
# from .views import DataCartList
from MyCapApp import views

from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('MyCapApp/', views.HousingDataList.as_view()),
    path('MyCapApp/', views.HousingDataDetail.as_view()),

]

