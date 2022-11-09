from rest_framework import permissions



class TeacherIsAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.subject.teacher.id or request.user.is_superuser:
            return True


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.user.id == obj.subject.teacher.id or request.user.is_superuser:
        return True     
        
class TeacherOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
        


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == "TEACHER"


class IsStudent(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == "STUDENT"
