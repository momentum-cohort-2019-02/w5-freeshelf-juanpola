from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from freeshelfapp.models import Book
from django.views import generic
# from 
import csv, io
# Create your views here.

def index(request):
     
     return render(request, 'index.html',)

def login(request):
    return render(request, 'login.html',)

# def 