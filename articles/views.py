from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
# from IPython import embed
from .models import Article, Comment
from django.contrib import messages

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
        'comments' : article.comment_set.all(),
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

@require_POST
def comment_create(request, article_pk):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.article_id = article_pk
    comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('articles:detail', article_pk)