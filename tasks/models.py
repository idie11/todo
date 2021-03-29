from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')
    deadline = models.DateTimeField('Deadline', null=True ) #нужно ли ставить автонауэд=тру?
    category = models.ForeignKey('categories.Category', models.CASCADE, 'task_cat') #on_delete каскаде или сет нуль
    user = models.ForeignKey('users.User', models.CASCADE, 'task_user')
