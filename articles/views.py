from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    ttl = request.GET.get('title')
    cntnt = request.GET.get('content')
    article = Article(title=ttl, content=cntnt)
    article.save()
    context = {
        'ttl': ttl,
        'cntnt': cntnt,
    }
    return render(request, 'articles/create.html', context)