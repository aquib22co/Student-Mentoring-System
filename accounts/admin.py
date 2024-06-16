from django.contrib import admin
from .models import Batch, Student, Teacher,Profile,Attendance,Marks,Message

admin.site.register(Batch)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Message)



