from django import forms
from article.models import Article
# from article.models import Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('__all__')
#         labels = {
#             'title': 'Custom Title',
#         }
