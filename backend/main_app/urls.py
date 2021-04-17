from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [

    path('addinfo/', AddStudentMoreView.as_view()),
    path('startpractice/', StartPracticeRequestView.as_view()),

    path('startcompany/', CreateCompanyView.as_view()),
    path('hirecompany/', AddEmployerView.as_view()),

    path('startorganization/', CreateOrganizationView.as_view()),
    path('hireorganization/', AddWorkerView.as_view()),

    path('createinternship/', CreateInternshipView.as_view()),

    path('applyinternship/<int:pk>/', ApplyForInternshipView.as_view()),
    path('inviteinternship/<int:pk>/', InviteForInternshipView.as_view()),
    path('adviceinternship/<int:pk>/', AdviceForInternshipView.as_view()),

    path('listinternship/', ListAvailableInternshipView.as_view()),

    path('createcompetence/', CreateCompetenceView.as_view()),

    path('createcompetence/', CreateCompetenceView.as_view()),

    path('companylist/', CompanyListView.as_view()),
    path('organizationlist/', OrganizationListView.as_view()),
    path('acceptinternship/', AcceptInternship.as_view()),

    # path('practice/list/', ListPracticeView.as_view()),

]
