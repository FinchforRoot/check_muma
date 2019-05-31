from django.db import models

# Create your models here.
class Python(models.Model):
    id = models.SmallIntegerField(max_length=8)
    url = models.CharField
    is_safe = models.CharField