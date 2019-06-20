from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse
from article.models import Article
from article.forms import ArticleForm

class IndexView(ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.all()[:2]

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     return context

# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'index.html',{'articles': articles})


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))
# def create(request):
#     form = ArticleForm()
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             created = form.save()
#         return redirect('detail', created.id)
#     return render(request, 'article/create.html', {'form': form})

# def detail(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'article/detail.html', {'article': article})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

class ArticleDeleteView(DetailView):
    model = Article
    success_url = '/'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'
    template_name = 'article/delete.html'