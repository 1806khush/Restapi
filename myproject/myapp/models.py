from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    """Model for code snippets"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, default='python')
    style = models.CharField(max_length=100, default='friendly')
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.title or f"Snippet {self.id}"


class Comment(models.Model):
    """Model for comments on snippets"""
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    snippet = models.ForeignKey(Snippet, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.snippet}"