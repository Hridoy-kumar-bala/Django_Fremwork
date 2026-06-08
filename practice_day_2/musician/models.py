from django.db import models
from album.models import Album
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =models.EmailField()
    phone =models.IntegerField()
    instrument_type =models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicians')
    def __str__(self):
        return self.first_name

