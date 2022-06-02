from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    user_id = models.IntegerField(default = 1)
