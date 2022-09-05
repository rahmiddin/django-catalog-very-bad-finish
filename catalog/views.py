from django.shortcuts import render
from .models import Book
# Create your views here.


def catalog_view(request):
    template = 'index.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template_name=template, context=context)