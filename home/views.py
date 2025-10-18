from django.shortcuts import render
from blog.models import Article, Category


# Create your views here.

def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/index.html', {'articles': articles, 'categories': categories})