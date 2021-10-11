from django.urls import path 
from . import views 
from .views import HousingDataList  


urlpatterns = [
    path('MyCapApp/', views.HousingDataList.as_view()),
    path('MyCapApp/<int:pk>/', views.HousingDataDetail.as_view()),
]

