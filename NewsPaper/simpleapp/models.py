from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(
        max_length=75,
        unique=True
        )
    text = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='category',
        )
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    class Meta:
        app_label = 'myapp2'


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    def __str__(self):
         return self.name.title()
    class Meta:
         app_label = 'myapp'

