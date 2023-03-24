from django import forms
from archive.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'thumbnail']
        labels = {
            'title': '제목',
            'content': '내용',
            'thumbnail': '대표 이미지',
        }