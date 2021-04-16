from rest_framework.permissions import BasePermission

from .models import CustomUser


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (staff)'

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(BasePermission):
    message = 'It is wrong neighborhood for u (owner)'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsStudent(BasePermission):
    message = 'It is wrong neighborhood for u (student)'

    def has_object_permission(self, request, view, obj):
        return request.user.type == CustomUser.Type.STUDENT


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (admin)'

    def has_object_permission(self, request, view, obj):
        return request.user.type == CustomUser.Type.ADMIN


class IsEmployer(BasePermission):
    message = 'It is wrong neighborhood for u (employer)'

    def has_object_permission(self, request, view, obj):
        return request.user.type == CustomUser.Type.EMPLOYER


class IsEdWorker(BasePermission):
    message = 'It is wrong neighborhood for u (edworker)'

    def has_object_permission(self, request, view, obj):
        return request.user.type == CustomUser.Type.EDWORKER
