from django.db import models
from test1.models import Post

# Create your models here.

class Comment(models.Model):
    rise = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.rise