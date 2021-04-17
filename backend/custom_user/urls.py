from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [

    path('delete/', DeleteMyselfView.as_view()),
    path('update/', UpdateMyselfView.as_view()),
    path('add/student/', AddStudentMoreView.as_view()),
    path('kek/', AddStudentMoreView.as_view()),
]
