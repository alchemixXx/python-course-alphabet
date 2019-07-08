from django import forms
from .models import ArticleComment

class CommentForm(forms.ModelForm):
    author = forms.EmailField(max_length=500)

    class Meta:
        model = ArticleComment
        fields = ('author', 'description')

        # labels = {
        #     'title': 'Comment Title',
        # }

