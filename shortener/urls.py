from django.urls import path
from shortener.views import CreateShortUrl, RetrieveOriginalURL, UpdateShortURL
urlpatterns = [
    path('shorten/', CreateShortUrl.as_view()),
    path('shorten/<str:short_code>/', RetrieveOriginalURL.as_view()),
    path('shorten/update/<str:short_code>/', UpdateShortURL.as_view()),

]