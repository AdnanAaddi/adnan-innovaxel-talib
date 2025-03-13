from django.shortcuts import render
from rest_framework.views import APIView
from .models import ShortenedURL
from .serializers import URLShortenerSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateShortUrl(APIView):
    """" Api to create a Short Url"""
    def post(self , request):
        serializer = URLShortenerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        