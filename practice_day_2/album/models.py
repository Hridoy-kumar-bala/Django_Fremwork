from django.db import models

# Create your models here.
RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_data = models.DateField()
    rating =models.IntegerField(choices= RATING_CHOICES, default= 1)
    def __str__(self):
        return self.name