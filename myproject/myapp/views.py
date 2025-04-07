from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .models import Snippet, Comment
from .serializers import SnippetSerializer, CommentSerializer, UserSerializer
from .permission import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    """
    List all comments for a snippet or create a new comment
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all comments for the snippet
        specified in the URL.
        """
        snippet_id = self.kwargs['snippet_id']
        return Comment.objects.filter(snippet__id=snippet_id)

    def perform_create(self, serializer):
        snippet_id = self.kwargs['snippet_id']
        serializer.save(
            author=self.request.user,
            snippet_id=snippet_id
        )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer