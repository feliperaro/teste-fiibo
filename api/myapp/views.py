from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataEntry
from .serializers import DataEntrySerializer

class DataView(APIView):
    def get(self):
        queryset = DataEntry.objects.all()
        serializer = DataEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uploaded successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
