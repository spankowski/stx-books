from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/vote/
    path('', views.books, name='books'),
    # ex: sort
    path('?published=<int:published_date>', views.published, name='published')
]