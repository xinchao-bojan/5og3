from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [

    path('addinfo/', AddStudentMoreView.as_view()),
    path('startpractice/', StartPracticeRequestView.as_view()),

    path('startcompany/', CreateCompanyView.as_view()),
    path('createinternship/', CreateInternshipView.as_view()),
    path('applyinternship/<int:pk>/', ApplyForInternship.as_view()),

    path('listinternship/', ListAvailableInternshipView.as_view()),

    # path('practice/list/', ListPracticeView.as_view()),

    path('test/', lol.as_view()),

]
