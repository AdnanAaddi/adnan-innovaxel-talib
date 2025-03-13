from rest_framework import serializers
from .models import ShortenedURL
class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code', 'created_at', 'updated_at', 'access_count']
        read_only_fields = ['short_code', 'created_at', 'updated_at', 'access_count']