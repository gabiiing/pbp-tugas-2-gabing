from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class WatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.CharField(max_length=100)
    review =  models.TextField()
