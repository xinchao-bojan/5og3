from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [

    path('addinfo/', AddStudentMoreView.as_view()),
    path('startpractice/', StartPracticeRequestView.as_view()),

    path('startcompany/', CreateCompanyView.as_view()),
    path('hirecompany/', AddEmployerView.as_view()),

    path('organization/create/', CreateOrganizationView.as_view()),  #
    path('organization/add_competence/', AddEdCompetence.as_view()),  #

    path('hireorganization/', AddWorkerView.as_view()),

    path('createinternship/', CreateInternshipView.as_view()),

    path('applyinternship/<int:pk>/', ApplyForInternshipView.as_view()),
    path('inviteinternship/<int:pk>/', InviteForInternshipView.as_view()),
    path('adviceinternship/<int:pk>/', AdviceForInternshipView.as_view()),

    path('listinternship/', ListAvailableInternshipView.as_view()),

    path('createcompetence/', CreateCompetenceView.as_view()),

    path('companylist/', CompanyListView.as_view()),
    path('organizationlist/', OrganizationListView.as_view()),
    path('acceptinternship/', AcceptInternship.as_view()),

    path('createpractice/', CreatePracticeView.as_view()),
    path('endpractice/', EndPracticeView.as_view()),
    path('applypractice/', ApplyForPracticeView.as_view()),

    path('detailpractice/<int:pk>/', DetailPracticeStudentView.as_view()),
    path('detailinternship/<int:pk>/', DetailInternshipStudentView.as_view()),

    path('practice/all/', ListPracticeView.as_view()),
    path('listallinternship/', ListInternshipView.as_view()),

    path('addskill/', AddSkillView.as_view()),

    path('oninternshipreview/<int:pk>/', CreateReviewOnInternshipView.as_view()),
    path('onstudentreview/<int:pk>/', CreateReviewOnStudentView.as_view()),

    # path('practice/list/', ListPracticeView.as_view()),

]
