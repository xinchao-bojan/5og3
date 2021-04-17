from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.exceptions import ValidationError

from custom_user.models import *
from .serializers import *
from custom_user.permissions import *
from custom_user.serializers import *


class ListPracticeView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent or IsEdWorker]
    serializer_class = PracticeSerializer
    queryset = None

    def get(self, request):
        print(StudentMore.objects.get(user=request.user))
        self.queryset = Practice.objects.filter(
            ed_organization=StudentMore.objects.get(user=request.user).ed_organization)
        return super().list(request)


class AddStudentMoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        try:
            if StudentMore.objects.get(user=request.user):
                return Response('already exist', status=status.HTTP_202_ACCEPTED)
        except StudentMore.DoesNotExist:
            try:
                request.user.type = CustomUser.Type.STUDENT
                request.user.save()
                more = StudentMore.objects.create(
                    user=request.user,
                    sex=request.data['sex'],
                    date_of_birth=request.data['date']
                )
                StudentM.objects.create(user=more,
                                        ed_organization=EdOrganization.objects.get(
                                            name=request.data['ed_organization']))
            except ValidationError:
                return Response('ValidationError', status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response('Key Error', status=status.HTTP_400_BAD_REQUEST)

            serializer = StudentSerializer(request.user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)


class StartPracticeRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request):
        o = StudentM.objects.get(user__user=request.user).ed_organization
        serializer = EdOrganizationSerializer(o.competence.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        u = StudentM.objects.get(user__user=request.user)
        if not u.ed_competence:
            return Response('lol')

        for c in request.data['ed_competence']:
            u.ed_competence.add(u.ed_organization.competence.get(pk=c['pk']))
        for c in request.data['emp_competence']:

            for elem in u.ed_competence.all():
                print(elem)
                for elem1 in elem.emp_competence.all():

                    s = EmpCompetence.objects.get(pk=c['pk'])

                    if elem1 == s:
                        u.emp_competence.add(s)

        serializer = StudentMSerializer(u, context={'request': request})
        return Response(serializer.data)


class ListAvailableInternshipView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]
    serializer_class = InternshipSerializer
    queryset = None

    # def get(self, request):
        

class lol(APIView):
    def get(self, request):
        return Response('xyu')
