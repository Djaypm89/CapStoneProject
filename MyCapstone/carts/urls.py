from django.urls import path 
from carts import views


urlpatterns = [
    path('', views.CartList.as_view()),
]