from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.exceptions import ValidationError

from .serializers import *
from custom_user.permissions import *
from custom_user.serializers import *

from custom_user.permissions import IsStudent, IsEdWorker


# class ListPracticeView(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated, IsStudent or IsEdWorker]
#     serializer_class = PracticeSerializer
#     queryset = None
#
#     def get(self, request):
#         print(StudentMore.objects.get(user=request.user))
#         self.queryset = Practice.objects.filter(
#             ed_organization=StudentMore.objects.get(user=request.user).ed_organization)
#         return super().list(request)
class CompanyListView(generics.ListAPIView):
    queryset = EmpCompany
    serializer_class = EmpCompanySerializer


class OrganizationListView(generics.ListAPIView):
    queryset = EdOrganization
    serializer_class = EdOrganizationSerializer


class AddStudentMoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        try:
            StudentMore.objects.get(user=request.user)
            return Response('already exist', status=status.HTTP_202_ACCEPTED)
        except StudentMore.DoesNotExist:
            try:
                d = {
                    'F': StudentMore.FEMALE,
                    'M': StudentMore.MALE
                }
                request.user.type = CustomUser.Type.STUDENT
                request.user.save()
                more = StudentMore.objects.create(
                    user=request.user,
                    sex=d[request.data['sex']],
                    date_of_birth=request.data['date']
                )
                print(request.data['ed_organization'])
                print(request.data)
                print(EdOrganization.objects.get(name='МИРЭА'))
                print(EdOrganization.objects.get(
                    name=request.data['ed_organization']))
                StudentM.objects.create(user=more,
                                        ed_organization=EdOrganization.objects.get(
                                            name=request.data['ed_organization']))
            except ValidationError:
                return Response('ValidationError', status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response('Key Error', status=status.HTTP_400_BAD_REQUEST)

            serializer = StudentSerializer(request.user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)


class StartPracticeRequestView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent or IsEdWorker]
    serializer_class = PracticeSerializer
    queryset = None

    def get(self, request):
        print(StudentMore.objects.get(user=request.user))
        self.queryset = Practice.objects.filter(
            ed_organization=StudentMore.objects.get(user=request.user).ed_organization)
        return super().list(request)

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

    def get(self, request):
        s = StudentM.objects.get(user=StudentMore.objects.get(user=request.user))

        internships_rate = dict.fromkeys(Internship.objects.all(), 0)

        internships_list = internships_rate.keys()

        sorted_internships = {}

        for internship in internships_list:
            for input_competence in internship.input_emp_competence.all():
                if input_competence in s.emp_competence.all():
                    internships_rate[internship] += 1

        sorted_internships_keys = sorted(internships_rate,
                                         key=internships_rate.get)
        for w in sorted_internships_keys:
            sorted_internships[w] = internships_rate[w]

        print(sorted_internships)

        serializer = InternshipSerializer(sorted_internships.keys(), context={'request': request}, many=True)
        return Response(serializer.data)


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


class AddEmployerView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def post(self, request):
        u = CustomUser.objects.get(pk=request.data['candidate'])
        u.type = CustomUser.Type.EMPLOYER
        u.save()
        c = EmployerM.objects.get(user=EmployerMore.objects.get(user=request.user)).emp_company
        m = EmployerMore.objects.create(user=u)
        em = EmployerM.objects.create(user=m, emp_company=c)
        serializer = EmployerMSerializer(em, context={'request': request})
        return Response(serializer.data)


class CreateOrganizationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            EdWorkerM.objects.get(user=request.user)
            return Response('already exist', status=status.HTTP_202_ACCEPTED)
        except EmployerMore.DoesNotExist:
            request.user.type = CustomUser.Type.EMPLOYER
            request.user.save()
            e = EdOrganization.objects.create(name=request.data['name'])
            m = EdWorkerMore.objects.create(user=request.user)
            em = EdWorkerM.objects.create(user=m, emp_company=e)
            serializer = EdWorkerMSerializer(em, context={'request': request})
            return Response(serializer.data)


class AddWorkerView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]

    def post(self, request):
        u = CustomUser.objects.get(pk=request.data['candidate'])
        u.type = CustomUser.Type.EDWORKER
        u.save()
        c = EdWorkerM.objects.get(user=EdWorkerMore.objects.get(user=request.user)).ed_organization
        m = EdWorkerMore.objects.create(user=u)
        em = EdWorkerM.objects.create(user=m, emp_company=c)
        serializer = EdWorkerMSerializer(em, context={'request': request})
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


class EndInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer, IsOwner]

    def post(self, request):
        e = EmployerM.objects.get(user=EmployerMore.objects.get(user=request.user))
        c = e.emp_company
        i = c.internship_set.get(pk=request.data['internship'])
        for u in request.data['students']:
            s = i.internshipapplication_set.get(pk=u['pk']).student
            s.emp_competence.add(i.input_emp_competence.all())
            s.emp_competence.add(i.output_emp_competence.all())
        return Response(status == status.HTTP_200_OK)


class ApplyForInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def put(self, request, pk):
        i = Internship.objects.get(pk=pk)
        s = StudentM.objects.get(user=StudentMore.objects.get(user=request.user))
        e = None
        if 'ed_organization' in request.data:
            e = EdOrganization.objects.get(pk=request.data['ed_organization'])

        i = InternshipApplication.objects.create(
            ed_organization=e,
            internship=i,
            student=s
        )
        serializer = InternshipApplicationSerializer(i, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class InviteForInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def put(self, request, pk):
        i = Internship.objects.get(pk=pk)
        s = StudentM.objects.get(pk=request.data['student'])

        i = InternshipApplication.objects.create(
            internship=i,
            student=s
        )
        serializer = InternshipApplicationSerializer(i, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdviceForInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]

    def put(self, request, pk):
        i = Internship.objects.get(pk=pk)
        e = EdWorkerM.objects.get(user=EdWorkerMore.objects.get(user=request.user))
        s = StudentM.objects.get(pk=request.data['student'])

        i = InternshipApplication.objects.create(
            internship=i,
            student=s,
            ed_organization=e.ed_organization
        )
        serializer = InternshipApplicationSerializer(i, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCompetenceView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def emp(self, request):
        queryset = []
        a = EmpCompetence.objects.create(name=request.data['name'])
        for ed in request.data['related']:
            a.edcompetence_set.add(EdCompetence.objects.get(pk=ed['pk']))
            queryset.append(a)
        a.save()
        return EmpCompetenceSerializer(queryset, many=True, context={'request': request})

    def ed(self, request):
        queryset = []
        a = EdCompetence.objects.create(name=request.data['name'])
        for emp in request.data['related']:
            a.emp_competence.add(EmpCompetence.objects.get(pk=emp['pk']))
            queryset.append(a)
        a.save()

        return EdCompetenceSerializer(queryset, many=True, context={'request': request})

    def post(self, request):
        d = {
            'emp': self.emp,
            'ed': self.ed,
        }
        serializer = d[request.data['type']](request)
        return Response(serializer.data)


class AcceptInternship(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def post(self, request, pk):
        i = InternshipApplication.objects.get(pk=pk)
        i.accepted = True
        i.save()
        return Response(i.student.user.user.email)


class CreatePracticeView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]

    def post(self, request):
        m = EdWorkerMore.objects.get(user=request.user)
        u = EdWorkerM.objects.get(user=m)
        i = Practice.objects.create(
            name=request.data['name'],
            ed_organization=u.ed_organization,
            description=request.data['description'])
        for input in request.data['input']:
            i.input_ed_competence.add(EdCompetence.objects.get(pk=input['pk']))
        for output in request.data['output']:
            i.output_ed_competence.add(EdCompetence.objects.get(pk=output['pk']))
        serializer = InternshipSerializer(i, context={'request': request})
        return Response(serializer.data)


class EndPracticeView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]

    def post(self, request):
        e = EdWorkerM.objects.get(user=EdWorkerMore.objects.get(user=request.user))
        c = e.ed_organization
        i = c.practice_set.get(pk=request.data['practice'])
        for u in request.data['students']:
            s = i.practiceapplication_set.get(pk=u['pk']).student
            s.ed_competence.add(i.input_ed_competence.all())
            s.ed_competence.add(i.output_ed_competence.all())
        return Response(status == status.HTTP_200_OK)


class ApplyForPracticeView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def put(self, request, pk):
        i = Practice.objects.get(pk=pk)
        s = StudentM.objects.get(user=StudentMore.objects.get(user=request.user))

        i = PracticeApplication.objects.create(
            practice=i,
            student=s
        )
        serializer = PracticeApplication(i, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailPracticeStudentView(generics.RetrieveAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]


class DetailInternshipStudentView(generics.RetrieveAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]


class ListInternshipView(generics.ListAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]


class ListPracticeView(generics.ListAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [permissions.IsAuthenticated, IsEdWorker]


class AddSkillView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def post(self, request):
        queryset = []
        for skillset in request.data['skillset']:
            s = Skill.objects.create(user=request.user, text=skillset['text'])
            queryset.append(s)
        serializer = SkillSerializer(s, context={'request': request})
        return Response(serializer.data)


class CreateReviewOnInternshipView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def post(self, request, pk):
        g = Internship.objects.get(pk=pk)
        ReviewOnStudent.objects.create(
            name=request.data['name'],
            review_text=request.data['review_text'],
            rate=request.data['rate'],
            student=StudentM.objects.get(user=StudentMore.objects.get(user=request.user)),
            goal=g
        )
        serializer = InternshipSerializer(g, context={'request': request})
        return Response(serializer.data)


class CreateReviewOnStudentView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def post(self, request, pk):
        g = StudentM.objects.get(pk=pk)
        ReviewOnStudent.objects.create(
            name=request.data['name'],
            review_text=request.data['review_text'],
            rate=request.data['rate'],
            employer=EmployerM.objects.get(user=EmployerMore.objects.get(user=request.user)),
            student_for_review=g
        )
        serializer = StudentM(g, context={'request': request})
        return Response(serializer.data)
