from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from config import settings


class Board(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)