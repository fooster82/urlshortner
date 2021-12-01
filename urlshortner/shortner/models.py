from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

class Url(models.Model):

    short_url = models.CharField(max_length=6, default='')
    original_url = models.URLField("URL", unique=True, default='')

    def make_url_small():
        short_url = get_random_string(length=6)    
        return short_url    

    def __str__(self):
        return f'The shorter url token is: {self.short_url}'