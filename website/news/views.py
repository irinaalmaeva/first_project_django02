from django.shortcuts import render
from .models import News_post


def news_home(request):
    return render(request, 'news/news_home.html')






# Create your views here.
