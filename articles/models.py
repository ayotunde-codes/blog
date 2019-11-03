from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    # author

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=1500)
    date = models.DateTimeField('date written', default=timezone.now)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # commenter