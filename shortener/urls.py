from django.urls import path
from shortener.views import CreateShortUrl
urlpatterns = [
    path('shorten/', CreateShortUrl.as_view()),

]