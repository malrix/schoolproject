from django.db import models

class Post(models.Model):
    """This model defines the concept of a Post in our blog."""

    title = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Пост')
        verbose_name_plural = ('Посты')


class Comment(models.Model):
    """A Comment a Post."""

    text = models.TextField()

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ('Коммент')
        verbose_name_plural = ('Комментарии')

def __str__(self):
        return self.title