from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    """Personal blog for author."""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts", verbose_name="Автор")
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return  f"{self.author} ({self.title}) ({self.text})"

