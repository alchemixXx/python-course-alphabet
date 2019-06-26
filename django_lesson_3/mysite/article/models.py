from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=Article)
def notify_author(sender, instance, **kwargs):
    subject = 'Artilce created'
    body = 'Your article created'
    send_from = settings.DEFAULT_FROM_EMAIL
    send_to = 'albert.li.das@gmail.com'
    send_mail(subject, body, send_from, [send_to] )