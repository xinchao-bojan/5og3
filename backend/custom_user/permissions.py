from rest_framework.permissions import BasePermission

from .models import CustomUser

def base(user):
    return bool(user and user.is_authenticated)


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (staff)'

    def has_permission(self, request, view):
        if base(request.user):
            return request.user.is_staff
        return False


class IsOwner(BasePermission):
    message = 'It is wrong neighborhood for u (owner)'

    def has_object_permission(self, request, view, obj):
        if base(request.user):
            return obj.user == request.user
        return False


class IsStudent(BasePermission):
    message = 'It is wrong neighborhood for u (student)'

    def has_object_permission(self, request, view, obj):
        if base(request.user):
            return request.user.type == CustomUser.Type.STUDENT
        return False


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (admin)'

    def has_object_permission(self, request, view, obj):
        if base(request.user):
            return request.user.type == CustomUser.Type.ADMIN
        return False


class IsEmployer(BasePermission):
    message = 'It is wrong neighborhood for u (employer)'

    def has_object_permission(self, request, view, obj):
        if base(request.user):
            return request.user.type == CustomUser.Type.EMPLOYER
        return False


class IsEdWorker(BasePermission):
    message = 'It is wrong neighborhood for u (edworker)'

    def has_object_permission(self, request, view, obj):
        if base(request.user):
            return request.user.type == CustomUser.Type.EDWORKER
        return False
