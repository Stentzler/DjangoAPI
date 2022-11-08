from rest_framework import permissions
import ipdb


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.teacher or request.user.is_superuser


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return False
        return request.user.role == "TEACHER"
