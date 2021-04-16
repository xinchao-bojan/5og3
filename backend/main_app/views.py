from django.shortcuts import render

from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, status, permissions

class ListEdOrganizationView(APIView):

class AddEdOrganizationView(APIView):

class DeleteEdOrganizationView(APIView):

class UpdateEdOrganizationView(APIView):



class ListEmpCompanyView(APIView):

class AddEmpCompanyView(APIView):

class DeleteEmpCompanyView(APIView):

class UpdateEmpCompanyView(APIView):



class ListPracticeView(APIView):
    def get(self, request):
        serializer = PracticeSerializer(Practice.objects.all())
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListEdOrganizationPracticeView(APIView):
    def get(self, request):
        serializer = PracticeSerializer(Practice.objects.filter(EdOrganization = request.ed_organization))
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddPracticeView(APIView):
    def post(self, request):
        p = Practice.objects.create(name=request.data['name'])
        return Response('Практика создана', status=status.HTTP_200_OK)

class DeletePracticeView(APIView):
    def delete(self, request, pr_id):
        p = Practice.objects.get(id=pr_id)
        p.delete()
        return Response('Практика удалена', status=status.HTTP_200_OK)

class UpdatePracticeView(APIView):
    def put(self, request, pr_id):
        p = Practice.objects.get(id=pr_id)
        p.

class ConfirmPracticeView(APIView):

class GiveCompetenceView(APIView):

class ListInternshipView(APIView):

class ResponseInternshipView(APIView):

class AcceptStudentOnInternshipView(APIView):

class CompleteInternship(APIView):