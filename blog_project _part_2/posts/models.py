from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    category =models.ManyToManyField(Category) #akta post multiple category takte pare abr akta category multiple post takte pare 
    author = models.ForeignKey(User,on_delete=models.CASCADE) # jodi amra author k delete kore dai tar sob post delete hoiye jabe
    # author = models.ForeignKey(Author,on_delete=models.SET_NULL) # jodi amra author k delete korai tai tar post takbe but author null dekhabe
    def __str__(self):
        return f"{self.tittle}"