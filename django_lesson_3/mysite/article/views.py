from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Article
from .forms import ArticleForm
from account.models import Profile
from comment.forms import CommentForm
from comment.models import ArticleComment
from django.shortcuts import render, redirect
from django.http import request, HttpRequest
from django.urls import resolve


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)



    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        article = self.get_object()
        context = super(ArticleDetailView, self).get_context_data()
        context['comments'] = ArticleComment.objects.filter(id=article.id)
        return context


class CreateArticleComment(CreateView):
    model = ArticleComment
    template_name = 'comment/new_comment.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'article_id'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        article = self.get_object()
        context = super().get_context_data(**kwargs)
        context['id'] = article.id
        print(article.id)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.article = self.get_object()
        self.object.article = self.article.id
        self.object.save()
        super(CreateArticleComment, self).form_valid(form)


    # def form_valid(self, form):
    #     article = self.get_object()
    #     form['article'] = article.id
    #     form.save()
    #     return super(CreateArticleComment, self).form_valid(form)

    # def post_valid(self, form):
    #     article = self.get_object()
    #     # article = Article.objects.all()
    #     comment_articlecomment = form.save(commit=False)
    #     form.article = article.id
    #     # articlecomment.article = article
    #     comment_articlecomment.save()
    #     # return reverse('detail', args=(self.object.id,))

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))



class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'
