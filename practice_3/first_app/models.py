from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    comments = models.TextField()
    
    email = models.EmailField()
    email_address = models.EmailField(null=True, blank=True)
    email_address2 = models.EmailField()

    message = models.CharField(max_length=100)

    agree = models.BooleanField(default=False)

    date = models.DateField()
    birth_date = models.DateField()

    value = models.DecimalField(max_digits=10, decimal_places=2)

    first_name = models.CharField(max_length=100)
    day = models.DateField()

    favorite_color = models.CharField(max_length=20)
    favorite_colour = models.CharField(max_length=20)
    favorite_colors = models.CharField(max_length=100)


# class FromPage(ModelForm):
#     class Meta:
#         model = MyModel
#         fields = '__all__'
    def __str__(self):
        return self.name