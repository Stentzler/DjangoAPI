from rest_framework import permissions


class  TeacherIsAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.user.id == obj.subject.teacher.id or request.user.is_superuser:
        return True     