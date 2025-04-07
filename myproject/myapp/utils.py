from django.http import JsonResponse
from .models import Snippet, Comment


def get_snippet_details(snippet_id):
    """
    Get details of a specific snippet
    
    Args:
        snippet_id: ID of the snippet to retrieve
        
    Returns:
        Dictionary with snippet details or None if not found
    """
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        return {
            'id': snippet.id,
            'title': snippet.title,
            'code': snippet.code,
            'language': snippet.language,
            'owner': snippet.owner.username,
            'created': snippet.created,
        }
    except Snippet.DoesNotExist:
        return None


def get_comments_for_snippet(snippet_id):
    """
    Get all comments for a specific snippet
    
    Args:
        snippet_id: ID of the snippet to retrieve comments for
        
    Returns:
        List of comments or empty list if snippet not found
    """
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        comments = snippet.comments.all()
        
        return [
            {
                'id': comment.id,
                'content': comment.content,
                'author': comment.author.username,
                'created': comment.created,
            }
            for comment in comments
        ]
    except Snippet.DoesNotExist:
        return []


def create_comment(snippet_id, content, author):
    """
    Create a new comment for a snippet
    
    Args:
        snippet_id: ID of the snippet to comment on
        content: Text content of the comment
        author: User creating the comment
        
    Returns:
        Created comment object or None if snippet not found
    """
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        comment = Comment.objects.create(
            snippet=snippet,
            content=content,
            author=author
        )
        return comment
    except Snippet.DoesNotExist:
        return None


def format_error_response(message, status=400):
    """
    Format error response in consistent JSON structure
    
    Args:
        message: Error message
        status: HTTP status code
        
    Returns:
        JsonResponse with error details
    """
    return JsonResponse(
        {'error': message}, 
        status=status
    )