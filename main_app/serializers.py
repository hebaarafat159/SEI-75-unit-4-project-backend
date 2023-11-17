from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Author, Photo, Request

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
    # 'author'
        fields = ['title', 'category', 'description', 'published_date']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'avatar_url']

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        # 'book'
        fields = ['url']
        
class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ['status']
        