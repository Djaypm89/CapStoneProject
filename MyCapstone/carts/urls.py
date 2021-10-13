from django.urls import path 
from carts import views


urlpatterns = [
    path('Carts', views.CartList.as_view()),
]