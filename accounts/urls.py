from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register"),
    path('students', views.students, name="students"),
    path('teacher', views.teacher, name="teachers"),
    path('display_student/', views.display_students, name="display_student"),
    path('display_marks/', views.display_marks, name="display_marks"),
    path('send_message/', views.send_message, name='send_message'),
    path('conversation/<str:recipient_username>/', views.conversation, name='conversation'),

]