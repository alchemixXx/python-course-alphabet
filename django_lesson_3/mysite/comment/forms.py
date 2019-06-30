from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')
        labels = {
            'title': 'Custom Title',
        }
