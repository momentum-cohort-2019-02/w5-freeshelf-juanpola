from django.db import models
from datetime import date
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    """ This class represents a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    book_urls = models.URLField(max_length=150, null=True)
    book_description = models.CharField(max_length=5000, null=True, blank=True)
    date_added = models.DateField('Date Added', auto_now_add=True)

    def __str__(self):
        """ String """
        return self.title
    







