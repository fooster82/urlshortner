from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

class Url(models.Model):

    short_url = models.CharField(max_length=6)
    original_url = models.CharField(max_length=1023)

    def make_url_small(self):
        self.short_url = 'random number'


    def __str__(self):
        return f'The shorter url is: {self.short_url}'