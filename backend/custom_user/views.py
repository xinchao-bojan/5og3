from django.shortcuts import render
from rest_framework.exceptions import ValidationError

from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.views import APIView
from rest_framework import generics, status, permissions


def pretty_serializer(request):
    d = {
        'STUDENT': StudentSerializer,
        'ADMIN': AdminSerializer,
        'EMPLOYER': EmployerSerializer,
        'EDWORKER': EdWorkerSerializer
    }
    return d[request.user.type](request.user, context={'request': request})


class DeleteMyselfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        request.user.is_active = False
        request.user.save()
        serializer = pretty_serializer(request)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateMyselfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        u = request.user
        try:
            if 'sex' in request.data:
                u.more.sex = request.data['sex']

            if 'date_of_brith' in request.data:
                u.more.date_of_brith = request.data['date_of_brith']

            if 'email' in request.data:
                u.email = request.data['email']

            if 'first_name' in request.data:
                u.first_name = request.data['first_name']

            if 'last_name' in request.data:
                u.last_name = request.data['last_name']

            if 'email' in request.data:
                u.sex = request.data['email']
        except KeyError:
            return Response('Key Error', status=status.HTTP_400_BAD_REQUEST)
        u.save()
        serializer = pretty_serializer(request)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def put(self, request):
        c = CustomUser.objects.get(pk=request.data['user'])
        if c.type == CustomUser.Type.ADMIN:
            return Response('already admin')
        c.type = CustomUser.Type.ADMIN
        AdminMore.objects.create(user=c)
        c.save()
        serializer = AdminSerializer(c, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
