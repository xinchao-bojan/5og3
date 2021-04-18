from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Employer)
admin.site.register(EdWorker)
