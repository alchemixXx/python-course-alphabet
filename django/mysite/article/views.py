from django.shortcuts import render, redirect
from django.views.generic import ListView
from article.models import Article
from article.forms import ArticleForm

class IndexView(ListView):
    model = Article
    template = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        return context

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html',{'articles': articles})

def create(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            created = form.save()
        return redirect('detail', created.id)
    return render(request, 'article/create.html', {'form': form})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article/detail.html', {'article': article})