from django.db import models
from account.models import Profile
from article.models import Article
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


# Create your models here.
class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)
    author = models.CharField(max_length=500, null=False, blank=False, help_text="Please enter valid email", )
    timespan_created = models.DateTimeField(default=datetime.now)
    timespan_updated = models.DateTimeField(auto_now=True)
    description = RichTextUploadingField(null=True, blank=True, help_text="Please enter the Body of Comment", )

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'

    def __str__(self):
        return "This is comment:" + self.description[:200]



