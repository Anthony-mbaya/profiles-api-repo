from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """check user trying to edit"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow user update wn prof"""

    def has_oject_permission(self, request, view, obj):
        """check if user is trying updadte own"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
