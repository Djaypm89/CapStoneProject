from django.urls import path 
from . import views 
from .views import HousingDataList
# from .views import DataCartList
from MyCapApp import views


urlpatterns = [
    path('MyCapApp/', views.HousingDataList.as_view()),
    path('MyCapApp/', views.HousingDataDetail.as_view()),
    # path('MyCapApp/<int:pk>/', views.HousingDataDetail.as_view()),

    # path('', views.DataCartList.as_view())

    # path('MyCapApp/', views.DataCartList.as_view())
]

