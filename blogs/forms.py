"""Module contains classes that helps create a form"""

from django import forms
from .models import BlogPostTitle, BlogContent

class BlogPostTitleForm(forms.ModelForm):
    class Meta:
        model=BlogPostTitle
        fields=['text']
        labels={'text': ''}

class BlogContentForm(forms.ModelForm):
    class Meta:
        model=BlogContent
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
        