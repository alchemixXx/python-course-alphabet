from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from account.models import Profile
from comment.forms import CommentForm
from django.shortcuts import render, redirect


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

    def add_comment(self, request):
        if request.method == "POST":
            article_id = request.POST.get('article_id')
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = form.author
                comment.description = form.description
                comment.save()
                return redirect('detail', article_id=article_id)
            # pass
        else:
            form = CommentForm()
        template_name = 'article/detail.html'
        context = {'form': form}
        return render(request, template_name, context)
        #     pass
        # pass


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
