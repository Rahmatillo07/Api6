from rest_framework.permissions import BasePermission,SAFE_METHODS

class OnlyAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff