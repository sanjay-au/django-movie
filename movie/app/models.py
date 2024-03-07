from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=40)
    director=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    image=models.FileField(upload_to='image',null=True,blank=True)
    def __str__(self):
        return self.title