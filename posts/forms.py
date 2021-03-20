from django import forms
from posts.models import Post, Follow


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text",]
        help_texts = {
            "text": ("Напишите текст"),
            "title": ("Напишите заголовок"),
        }


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ["user"]
