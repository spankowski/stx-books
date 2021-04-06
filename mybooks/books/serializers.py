from rest_framework import serializers
from .models import Book, Author, Category

class CategorySeializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model = Category
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    #def to_representation(self, value):
    #     return value.author_first_name + " " + value.author_last_name
    class Meta:
        model = Author
        fields = ['author_first_name','author_last_name']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()
    categories = CategorySeializer()
    class Meta:
        model = Book
        fields = ['title','authors','categories','published_date']

    def create(self, validated_data):
        data = validated_data
        #authors_data = validated_data.pop('authors')
        #print(authors_data)
        print('Debug')
        print(validated_data)
        #categories_data = validated_data.pop('categories')
        #book = Book.objects.create(**validated_data)
        #for author_data in authors_data:
        #    Author.objects.create(book=book, **author_data)
        # for category_data in categories_data:
        #     Category.objects.create(book=book, **category_data)
        return data    