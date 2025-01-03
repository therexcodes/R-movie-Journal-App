from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=220)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_id = models.CharField(max_length=20, unique=True)
    plot = models.TextField()
    year = models.CharField(max_length=4)
    
    
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    movies = models.ManyToManyField(Movie, related_name='tags')
    
    
class FavouriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    
class Stats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_movie_watched = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    

    