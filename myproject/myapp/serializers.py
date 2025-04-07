from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model"""
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'created', 'content', 'author', 'snippet']


class SnippetSerializer(serializers.ModelSerializer):
    """Serializer for Snippet model"""
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'comments']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']