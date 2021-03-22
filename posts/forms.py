from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    """Form post."""
    class Meta:
        model = Post
        fields = ["title", "text"]
        help_texts = {
            "text": ("Напишите текст"),
            "title": ("Напишите заголовок")
        }


# class FollowForm(forms.ModelForm):
#     class Meta:
#         model = Follow
#         fields = ["user"]

class EmailForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        label='Текст',
        widget=forms.TextInput(attrs={'class': 'form-control', "rows": 5}))
