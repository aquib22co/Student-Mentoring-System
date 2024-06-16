from django import forms
from .models import Student, Teacher, Message

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rollno', 'dob', 'address', 'phone', 'batch', 'teacher']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'batch']

class MessageForm(forms.Form):
    recipient = forms.CharField(label='Recipient')
    content = forms.CharField(widget=forms.Textarea, label='Message')