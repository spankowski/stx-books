from django.db import models
# Create your models here.

class Author(models.Model):
    author_first_name = models.CharField(max_length=255, blank=False)
    author_last_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.author_first_name + " " +  self.author_last_name


class Category(models.Model):
    name = models.CharField(max_length=20, default="book") 
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=38, default="Title")
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.DateField(blank=True, null=True, default=None)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.DecimalField(default=0,  max_digits=3, decimal_places=2)
    ratings_count = models.DecimalField(default=0,  max_digits=5, decimal_places=0)
    thumbnail = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title