from django import forms
from .models import ArticleComment

class CommentForm(forms.ModelForm):

    article_id = forms.IntegerField(widget=forms.HiddenInput)
    author = forms.EmailField(max_length=500)

    class Meta:
        model = ArticleComment
        fields = '__all__'

        # labels = {
        #     'title': 'Comment Title',
        # }

