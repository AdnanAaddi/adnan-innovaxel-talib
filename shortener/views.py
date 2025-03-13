from django.shortcuts import render
from rest_framework.views import APIView
from .models import ShortenedURL
from .serializers import URLShortenerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateShortUrl(APIView):
    """" Api to create a Short Url"""
    def post(self , request):
        serializer = URLShortenerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveOriginalURL(APIView):
    """API to retrieve the original URL from a short code."""
    def get(self, request, short_code):
        url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
        url_entry.access_count += 1
        url_entry.save()
        data = URLShortenerSerializer(url_entry).data
        data.pop("access_count",None)
        return Response(data)

        