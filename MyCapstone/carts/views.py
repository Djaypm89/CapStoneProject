from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Cart
from .serializers import CartSerializer
from django.contrib.auth.models import User

# Create your views here.
class CartList(APIView):

    permission_classes = [AllowAny]
    # change to [IsAuthenticated for saved data shopping cart model where reqs userId]
    
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)