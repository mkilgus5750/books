from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    genre = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
