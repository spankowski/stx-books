from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse

# Create your views here.
def books(request):
    latest_books_list = Book.objects.order_by('-published_date')[:5]
    output = ''.join([f"{b.title}<br>" for b in latest_books_list])
    return HttpResponse(output) 


def published(request, published_date):
    book = get_object_or_404(Book, pk=published_date)
    return render(request, 'publshed.html', {'book': book})    