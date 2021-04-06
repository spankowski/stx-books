from django.shortcuts import render, get_object_or_404
from .models import Book, Category, Author
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BookSerializer
from django.db.models import Q #
from operator import and_ #
from functools import reduce #
# Create your views here.
def books(request):
    latest_books_list = Book.objects.order_by('-published_date')[:5]
    output = ''.join([f"{b.title}<br>" for b in latest_books_list])
    return HttpResponse(output) 


def published(request, published_date):
    book = get_object_or_404(Book, pk=published_date)
    return render(request, 'publshed.html', {'book': book})    

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookViewSetParam(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    # def post(self, request, *args, **kwargs):
    #     book_data = request.data
    #     new_book = Book.objects.create(title=book_data["title"], 
    #     authors = Author.create(author_first_name = book_data['author_first_name'], 
    #                             author_last_name = book_data['author_last_name']))
    #     # published_date=book_data["published_date"])

    #     new_book.save()

    #     serializer = BookSerializer(new_book)

    #     return Response(serializer.data)
 

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        category = self.request.query_params.get('categories')
        author = self.request.query_params.getlist('authors')
        published = self.request.query_params.get('published_date')
        sort = self.request.query_params.get('sort')
        # print(published)
        if title is not None:
            queryset = queryset.filter(title=title)
        elif category is not None:
            queryset = queryset.filter(categories__name=category)
        elif published is not None:
            queryset = queryset.filter(published_date=published)
        elif sort is not None:
            queryset = queryset.order_by(sort) 
        elif author: 
            for a in author:
                queryset = queryset.filter(authors__author_first_name=a)
                if not queryset:
                    break
        return queryset