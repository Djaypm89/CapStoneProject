from django.http.response import Http404
from rest_framework import serializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import HousingData
from .serializers import HousingDataSerializer
# from .models import DataCart
# from .serializers import DataCartSerializer
from django.contrib.auth.models import User



# Create your views here.
class HousingDataList(APIView):

    permission_classes = [AllowAny]
    # change to [IsAuthenticated for saved data shopping cart model where reqs userId]
    
    def get(self, request):
        stats = HousingData.objects.all()
        serializer = HousingDataSerializer(stats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HousingDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HousingDataDetail(APIView):

    def get_object(self,pk):
        try:
            return HousingData.objects.get(pk=pk)
        except HousingData.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        housingdata = self.get_object(pk)
        serializer = HousingDataSerializer(housingdata)
        return Response(serializer.data)

    def put(self, request, pk):
        housingdata = self.get_object(pk)
        serializer = HousingDataSerializer(housingdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        housingdata = self.get_object(pk)
        housingdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DataCartList(APIView):

#     permission_classes = [AllowAny]
#     # change to [IsAuthenticated for saved data shopping cart model where reqs userId]
    
#     def get(self, request):
#         stats = DataCart.objects.all()
#         serializer = DataCartSerializer(DataCart, many=True)
#         return Response(serializer.data)