from django.db import models
from django.core.validators import MinValueValidator

class Post(models.Model):
    name = models.CharField(
        max_length=75,
        unique=True
        )
    text = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='post',
        )
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


    class Category(models.Model):
        name = models.CharField(max_length=15, unique=True)
        def __str__(self):
            return self.name.title()

# Create your models here.
