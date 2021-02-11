from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Font(models.Model):
    name = models.CharField(max_length=100)


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Риэлтор')
    name = models.CharField(max_length=100)
    text = models.TextField()
    colorArea = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    font = models.ForeignKey(Font, on_delete=models.CASCADE)
    colorText = models.CharField(max_length=50)
