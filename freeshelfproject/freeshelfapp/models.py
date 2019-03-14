from django.db import models
from datetime import date , datetime
from django.template.defaultfilters import slugify
from django.urls import reverse
from slugger import AutoSlugField 
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    """ This class represents a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    slugger = AutoSlugField(unique=True, populate_from="title", blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    book_urls = models.URLField(max_length=150, null=True)
    book_description = models.CharField(max_length=5000, null=True, blank=True)
    date_added = models.DateField('Date Added', auto_now_add=True)
    book_image= models.ImageField(upload_to="book_image", blank="true")
    Favorited_by_user= models.ManyToManyField(to=User, related_name='favorites')

    # def get_absolute_url(self):
    #     return ('book_post_detial', (),
    #             {
    #         'slug': self.slug,
    #     })

    # def save(self, *args, **kwargs):
    #     if not self.title:
    #         self.slug = slugger(self.title)
    #     super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Category(models.Model):
    """This model is representing a category. """
    title = models.CharField(max_length= 200, blank = True )
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    programming_language = models.CharField(max_length=500, blank = True)
    date_added= models.DateTimeField(auto_now_add=True)
    # slugger = AutoSlugField(unique=True, populate_from="title")

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite' )
    book = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
