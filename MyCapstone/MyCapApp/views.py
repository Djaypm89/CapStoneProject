
from .models import HousingData
from .serializers import HousingDataSerializer
# from django import APIView
# from django import Response
# from django import status
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status

# Create your views here.
class HousingDataList(APIView):
    
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