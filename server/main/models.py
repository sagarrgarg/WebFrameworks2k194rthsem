from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    genre = models.ForeignKey('Genre',to_field='name', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(default=0)
    description = models.TextField()
    published_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Comment (models.Model):
    user = models.ForeignKey('auth.User',to_field='username', on_delete=models.CASCADE)
    book = models.ForeignKey('Book',to_field='name', on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)