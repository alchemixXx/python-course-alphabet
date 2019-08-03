from django.contrib import admin
from .models import ArticleComment, CommentOnComment

# Register your models here.
admin.site.register(ArticleComment)
admin.site.register(CommentOnComment)