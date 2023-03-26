from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)