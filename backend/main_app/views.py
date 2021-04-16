from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions

from custom_user.models import *
from .serializers import *
from custom_user.permissions import *


#
#
# class ListEdOrganizationView(APIView):
#
#
# class AddEdOrganizationView(APIView):
#
#
# class DeleteEdOrganizationView(APIView):
#
#
# class UpdateEdOrganizationView(APIView):
#
#
# class ListEmpCompanyView(APIView):
#
#
# class AddEmpCompanyView(APIView):
#
#
# class DeleteEmpCompanyView(APIView):
#
#
# class UpdateEmpCompanyView(APIView):
#
#
# class AddPracticeView(APIView):
#
#
# class DeletePracticeView(APIView):
#
#
# class UpdatePracticeView(APIView):


class ListPracticeView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = PracticeSerializer
    queryset = None

    def get(self, request):
        print(StudentMore.objects.get(user=request.user))
        self.queryset = Practice.objects.filter(
            ed_organization=StudentMore.objects.get(user=request.user).ed_organization)
        return super().list(request)
