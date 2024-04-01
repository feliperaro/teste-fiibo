from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataEntry
from .serializers import DataEntrySerializer
from rest_framework.renderers import JSONRenderer

class DataView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = DataEntry.objects.all()
        serializer = DataEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uploaded successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
