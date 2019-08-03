from django import forms
from .models import ArticleComment, CommentOnComment


class CommentForm(forms.ModelForm):
    author = forms.EmailField(max_length=500)

    class Meta:
        model = ArticleComment
        fields = ('author', 'description')

        labels = {
            'author': 'Author Email',
            'description': "Enter your comment:"
        }


class CommentOnCommentForm(forms.ModelForm):
    author = forms.EmailField(max_length=150)
    # comment = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = CommentOnComment
        fields = ('author', 'description')
