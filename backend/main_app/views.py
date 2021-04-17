from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions

from custom_user.models import *
from .serializers import *
from custom_user.permissions import *


class ListPracticeView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent or IsEdWorker]
    serializer_class = PracticeSerializer
    queryset = None

    def get(self, request):
        print(StudentMore.objects.get(user=request.user))
        self.queryset = Practice.objects.filter(
            ed_organization=StudentMore.objects.get(user=request.user).ed_organization)
        return super().list(request)


class StartPracticeRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]


