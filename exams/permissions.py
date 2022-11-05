from rest_framework import permissions

class  IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.teacher or request.user.is_superuser