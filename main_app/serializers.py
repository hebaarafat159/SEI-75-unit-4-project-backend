from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Author, Photo, BookRequest, Customer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'id', 'password']
    
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        if not value:
            return value
        return make_password(value)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user =  UserSerializer(read_only=True)
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ['user','location']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'avatar_url']

class BookSerializer(serializers.ModelSerializer):
    author =  AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'
# ['title', 'category', 'description', 'published_date', 'cover_image', 'author']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # 'book'
        fields = ['url']
        
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = ['status']
        