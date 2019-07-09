from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Article
from .forms import ArticleForm
from account.models import Profile
from comment.forms import CommentForm, CommentOnCommentForm
from comment.models import ArticleComment, CommentOnComment
from django.shortcuts import render, redirect
from django.http import request, HttpRequest
from django.urls import resolve
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import re


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
        # context['comments'] = ArticleComment.objects.filter(article_id=article.id)
        all_comments = ArticleComment.objects.filter(article_id=article.id)
        all_second_comments = CommentOnComment.objects.all()
        paginator = Paginator(all_comments, 5)
        page = self.request.GET.get('page')
        comments = paginator.get_page(page)
        context['comments'] = comments
        context['second_comments'] = all_second_comments
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
        context['article'] = article
        if self.request.user.is_authenticated:
            self.nickname = self.request.user.username
            self.user = User.objects.filter(username=self.nickname)[0]
            context['author_email'] = self.user.email
            context['author_nickname'] =self.nickname
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.article = self.get_object()
        self.actual_article = Article.objects.filter(id=self.article.id)
        self.object.article = self.actual_article[0]
        self.object.save()
        return super(CreateArticleComment, self).form_valid(form)

    def form_invalid(self, form):
        print('This form is invalid')

    def get_success_url(self):
        return reverse('detail', args=(self.article.id,))

class CreateCommentOnComment(CreateView):
    model = CommentOnComment
    template_name = 'comment/new_comment_on_comment.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_id'
    form_class = CommentOnCommentForm

    def get_context_data(self, **kwargs):
        comment = self.get_object(queryset=ArticleComment.objects.all())
        context = super().get_context_data(**kwargs)
        context['id'] = comment.id
        context['origin_comment'] = comment
        if self.request.user.is_authenticated:
            self.nickname = self.request.user.username
            self.user = User.objects.filter(username=self.nickname)[0]
            context['author_email'] = self.user.email
            context['author_nickname'] =self.nickname
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.comment = self.get_object(queryset=ArticleComment.objects.all())
        self.actual_comment = ArticleComment.objects.filter(id=self.comment.id)
        self.object.comment = self.actual_comment[0]
        self.object.save()
        return super(CreateCommentOnComment, self).form_valid(form)

    def form_invalid(self, form):
        print('This form is invalid')

    def get_success_url(self):
        # return reverse('detail', args=(self.article.id,))
        return reverse('index')


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
