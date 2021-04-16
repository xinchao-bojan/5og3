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
        serializer = PracticeSerializer(Practice.)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def



class AddPracticeView(APIView):
    def post(self, request):


class DeletePracticeView(APIView):

class UpdatePracticeView(APIView):

class ConfirmPracticeView(APIView):

class GiveCompetenceView(APIView):

class ListInternshipView(APIView):

class ResponseInternshipView(APIView):

class AcceptStudentOnInternshipView(APIView):

class CompleteInternship(APIView):