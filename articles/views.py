from django.shortcuts import render, redirect
# from IPython import embed
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles

    }
    # embed()
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        # 받아오는 로직
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 저장하는 로직
        article = Article(title = title, content = content)
        article.save()
        # 전달하는 로직
        context = {
            'article' : article,
        }
        # embed()
        # return render(request, 'articles/create.html', context)
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# from django.views.decorators.http import require_POST

# @require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article' : article,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article_pk)  
    else:
        article = Article.objects.get(pk=article_pk)
        context = {
            'article' : article,
        }
        return render(request, 'articles/edit.html', context)