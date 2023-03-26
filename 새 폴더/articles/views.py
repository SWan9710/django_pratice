from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.
def index(request):
    article = Articles.objects.all()
    context = {'article' : article}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticlesForm()
    context = {'form' : form}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticlesForm(instance=article)
    context = {'article' : article, 'form' : form}
    return render(request, 'articles/update.html', context)


def delete(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')