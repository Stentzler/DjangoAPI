from rest_framework import permissions


class  StudentIsAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.user.id == obj or request.user.is_superuser:
        return True
           
        