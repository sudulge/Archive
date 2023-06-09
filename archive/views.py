from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    article_list = Article.objects.order_by('-create_date')
    context = {'article_list': article_list}
    return render(request, 'archive/article_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'archive/article_detail.html', context)

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.create_date = timezone.now()
            article.save()
            return redirect('archive:index')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'archive/article_form.html', context)


#@login_required(login_url='common:login') 로그인이 필요한 함수. 
def article_modify(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    print(article.title)
    print(article.content)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.modify_date = timezone.now()
            article.save()
            return redirect('archive:detail', article_id=article_id)
    else:
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request, 'archive/article_form.html', context)