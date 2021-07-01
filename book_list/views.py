from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import BookForm
from .models import Book
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# Create your views here.

class BookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_list/book.html'
    success_url = '/submitted'

class BookList(ListView):
    template_name = 'book_list/books.html'
    model = Book
    context_object_name = "books"

class BookDetail(DetailView):
    template_name = 'book_list/book_detail.html'
    model = Book

class SubmittedView(TemplateView):
    template_name = 'book_list/submitted.html'