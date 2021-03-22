from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint, CheckConstraint, Q, F
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Personal blog for author."""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts", verbose_name="Автор")
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    read_post = models.ManyToManyField(User, related_name="read_post", blank=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return  f"{self.author} ({self.title}) ({self.text})"


class Follow(models.Model):
    """Model for subscribe."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )


    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ('author',)
        constraints = [
            UniqueConstraint(
                fields=["user", "author"],
                name='unique_follow'),
            CheckConstraint(
                check=~Q(user=F("author")),
                name="user_not_author",
            )]
