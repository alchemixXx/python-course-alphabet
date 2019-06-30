from django.shortcuts import render
from mysite.comment.models import Comment

# Create your views here.
class CommentView(ListView):
    model = Comment
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context