from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content', 'date', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
