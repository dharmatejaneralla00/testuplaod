from django.db import models


# Create your models here.

class Model(models.Model):
    name = models.CharField(max_length=10)
    files = models.FileField(upload_to='files/', default=None, null=True)
