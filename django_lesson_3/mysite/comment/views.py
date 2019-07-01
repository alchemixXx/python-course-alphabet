from django.shortcuts import render
from django.urls import reverse
from .models import Comment
from django.views.generic import ListView, CreateView
# from article.views import DetailView
from .forms import CommentForm
from .models import Article


# Create your views here.
class CommentView(ListView):
    model = Comment
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Comment.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommentView, self).get_context_data()
        return context


class NewCommentView(CreateView):
    # article_id = Article.objects.get('article_id')
    model = Comment
    template_name = 'comment/new_comment.html'
    context_object_name = 'comment'
    # pk_url_kwarg = 'article_id'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('index',)
