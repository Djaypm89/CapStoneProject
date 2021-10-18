
from . import views 
from .views import HousingDataList
# from .views import DataCartList
from MyCapApp import views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.HousingDataList.as_view()),
    # path('MyCapAppDetails/', views.HousingDataDetail.as_view()),
    path('<int:pk>/', views.HousingDataDetail.as_view()),

]

