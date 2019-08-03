from django.shortcuts import render
from django.urls import reverse
from .models import Comment
from django.views.generic import ListView, CreateView
# from article.views import DetailView
from .forms import CommentForm
from .models import Article

