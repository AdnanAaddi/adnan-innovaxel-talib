from django.urls import path
from shortener.views import CreateShortUrl, RetrieveOriginalURL
urlpatterns = [
    path('shorten/', CreateShortUrl.as_view()),
    path('shorten/<str:short_code>/', RetrieveOriginalURL.as_view()),

]