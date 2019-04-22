from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Genre, Book, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','username',
                    'password','is_active','is_superuser')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name','description')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'genre', 'author', 'pages', 'description', 'published_on')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'comment', 'created_on')