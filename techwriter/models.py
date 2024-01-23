from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    industry_type = models.CharField(max_length=100)
    preferences = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clients'


class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Status'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Rich text field can be implemented using a third-party package like django-ckeditor
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='articles')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='articles')
    deadline = models.DateField()
    last_modification_date = models.DateField(auto_now=True)
    # Additional fields like categories, tags, and comments can be added as needed

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Articles'

