from django.urls import path 
from . import views 


urlpatterns = [path('MyCapApp/', views.HousingDataList.as_view()),
]