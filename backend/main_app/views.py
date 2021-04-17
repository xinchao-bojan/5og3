from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.exceptions import ValidationError

from .serializers import *
from custom_user.permissions import *
from custom_user.serializers import *

from custom_user.permissions import IsStudent, IsEdWorker


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
            StudentMore.objects.get(user=request.user)
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


class CreateCompanyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            EmployerMore.objects.get(user=request.user)
            return Response('already exist', status=status.HTTP_202_ACCEPTED)
        except EmployerMore.DoesNotExist:
            request.user.type = CustomUser.Type.EMPLOYER
            request.user.save()
            e = EmpCompany.objects.create(name=request.data['name'])
            m = EmployerMore.objects.create(user=request.user)
            em = EmployerM.objects.create(user=m, emp_company=e)
            serializer = EmployerMSerializer(em, context={'request': request})
            return Response(serializer.data)


class CreateInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def post(self, request):
        m = EmployerMore.objects.get(user=request.user)
        u = EmployerM.objects.get(user=m)
        i = Internship.objects.create(
            name=request.data['name'],
            emp_company=u.emp_company,
            description=request.data['description'])
        for input in request.data['input']:
            i.input_emp_competence.add(EmpCompetence.objects.get(pk=input['pk']))
        for output in request.data['output']:
            i.output_emp_competence.add(EmpCompetence.objects.get(pk=output['pk']))
        serializer = InternshipSerializer(i, context={'request': request})
        return Response(serializer.data)


class ApplyForInternship(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def put(self, request, pk):
        i = Internship.objects.get(pk=pk)
        s = StudentM.objects.get(user=StudentMore.objects.get(user=request.user))
        i.students.add(s)
        return Response(status=status.HTTP_200_OK)


class lol(APIView):
    def get(self, request):
        d = [
            {
                'id': 1,
                'first_name': 'Ivan',
                'last_name': 'Malov',
                'date': '06-16-2001',
                'sex': 1,
                'email': 'sosu@xyu.ru',
                'organization': {
                    'name': 'SAS',
                    'description': 'sasi xyu'
                }
            },
            {
                'id': 2,
                'first_name': 'MAx',
                'last_name': 'Garshin',
                'date': '06-16-2001',
                'sex': 1,
                'email': 'sosu@xyu.ru',
                'organization': {
                    'name': 'SAS',
                    'description': 'sasi xyu'
                }
            }
        ]
        return Response(d)
