from django.contrib.auth.models import User
from django.db import models

class Batch(models.Model):
    department = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    batch_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.department} - {self.year} - Batch {self.batch_no}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    rollno = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.PositiveIntegerField()
    absent = models.PositiveIntegerField()

class Marks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    AOA = models.PositiveIntegerField()
    Maths = models.PositiveIntegerField()
    DBMS = models.PositiveIntegerField()
    MP = models.PositiveIntegerField()
    OS = models.PositiveIntegerField()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.recipient.username}: {self.content[:20]}..."