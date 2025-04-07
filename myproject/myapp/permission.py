from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # For Snippet objects, check if the user is the owner
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        
        # For Comment objects, check if the user is the author
        if hasattr(obj, 'author'):
            return obj.author == request.user
            
        return False