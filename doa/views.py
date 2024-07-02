from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doa
from .serializers import DoaSerializer

class DoaList(APIView):
    def get(self, request):
        doas = Doa.objects.all()
        serializer = DoaSerializer(doas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoaDetail(APIView):
    def get(self, request, pk):
        try:
            doa = Doa.objects.get(pk=pk)
        except Doa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoaSerializer(doa)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            doa = Doa.objects.get(pk=pk)
        except Doa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoaSerializer(doa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            doa = Doa.objects.get(pk=pk)
        except Doa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        doa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
