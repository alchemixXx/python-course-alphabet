from django.db import models
from account.models import Profile
from article.models import Article
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    author = models.CharField(max_length=500, null=True, blank=True)
    timespan_created = models.DateTimeField(default=datetime.now, blank=True)
    timespan_updated = models.DateTimeField(default=datetime.now, blank=True)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.author, self.timespan_created, self.description[:200]

