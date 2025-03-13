import random
import string
from django.db import models

def generate_short_code():
    """Generate  randomm 6-characters short code..........."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

