from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles

    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 받아오는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 저장하는 로직
    article = Article(title = title, content = content)
    article.save()
    # 전달하는 로직
    context = {
        'article' : article,
    }
    return render(request, 'articles/create.html', context)