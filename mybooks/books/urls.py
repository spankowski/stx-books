from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, BookViewSetParam

router = routers.DefaultRouter()
router.register('books',BookViewSet)
router.register('booksparam', BookViewSetParam, basename='MyModel')

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/vote/
    #path('', views.books, name='books'),
    path('', include(router.urls)),

    # ex: sort
    # path('?published=<int:published_date>', views.published, name='published')
]