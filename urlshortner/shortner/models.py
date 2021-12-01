from django.db import models

# Create your models here.

class Url(models.Model):

    short_url = models.CharField(max_length=6)
    original_url = models.CharField(max_length=1023)

    def __str__(self):
        return f'The shorter url is: {self.short_url}'