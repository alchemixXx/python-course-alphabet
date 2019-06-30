from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    timespan_created = models.DateTimeField(auto_now_add=True)
    timespan_updated = models.DateTimeField(auto_now=True)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.author, self.timespan_created
