from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [
    path('practice/list/', ListPracticeView.as_view()),

]