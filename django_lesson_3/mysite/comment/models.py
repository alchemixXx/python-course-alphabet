from django.db import models
from account.models import Profile
from article.models import Article
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


# Create your models here.
class ArticleComment(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)
    author = models.CharField(max_length=500, null=False, blank=False)
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    timespan_created = models.DateTimeField(auto_now_add=True)
    timespan_updated = models.DateTimeField(auto_now=True)
    description = RichTextUploadingField(null=True, blank=True)

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'

    def __str__(self):
        return self.author, self.timespan_created, self.description[:200]

