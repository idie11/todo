from django.db import models


class Category(models.Model):
    name = models.CharField('Name of category', max_length=150)
    description = models.TextField('Description') 
    user = models.ForeignKey('users.User', models.CASCADE, 'category')