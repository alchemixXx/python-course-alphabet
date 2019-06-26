from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    author = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }
