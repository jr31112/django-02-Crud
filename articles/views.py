from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from IPython import embed
from .models import Article, Comment
from django.contrib import messages
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    # embed()
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
    # POST 요청 -> 검증 및 저장
        article_form = ArticleForm(request.POST)
        # embed()
        if article_form.is_valid():
        # 검증에 성공하면 저장하고,
            # title = article_form.cleaned_data.get('title')
            # content = article_form.cleaned_data.get('content')
            # article = Article(title = title, content = content)
            article = article_form.save(commit=False)
            article.image = request.FILES.get('image')
            article.save()
            # redirect
            return redirect('articles:detail', article.pk)
    else:
    # GET 요청 -> Form
        article_form = ArticleForm()
    # GET -> 비어있는 Form context
    # POST -> 검증 실패시 에러메시지와 입력값 채워진 Form context
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : article.comment_set.all(),
        'comment_form' : comment_form,
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
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
        return redirect('articles:detail', article_pk)  
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 1. modleform에 사용자 입력값 넣고
    comment_form = CommentForm(request.POST)

    # 2. 검증하고,
    if comment_form.is_valid():
    # 3. 맞으면 저장
        # 3-1. 사용자 입력값으로 comment instance 생성(저장은 x)
        comment = comment_form.save(commit=False)
        # 3-2. Foreign Key 넣고 저장
        comment.article = article
        comment.save()
    # 4. return redirect
    else:
        messages.success(request, '댓글이 형식에 맞지 않습니다.')
    return redirect('articles:detail', article_pk)
    # comment = Comment()
    # comment.content = request.POST.get('content')
    # comment.article = article
    # comment.save()
    # return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('articles:detail', article_pk)