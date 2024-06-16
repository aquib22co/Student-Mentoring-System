from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Student, Teacher,Marks,Message
from django.contrib.auth.models import User
from .forms import StudentForm, TeacherForm, MessageForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user=user)  # Get the user's profile
            if profile.is_student:
                return redirect('students')  # Redirect to the students view
            else:
                return redirect('teachers') # Redirect to the teachers view
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('login')     
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):               # Logs out the user and redirects to the home page

    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            # Create a profile for the user
            profile = Profile.objects.create(user=user)
            
            # Set user type based on form input
            user_type = request.POST.get('user_type')
            if user_type == 'student':
                profile.is_student = True
                profile.save()
            else:
                profile.is_student = False
                profile.save()
            
            # Log in the user and redirect based on user type
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful.")
            
            return render(request,"index.html")
   
    else:
        form = UserCreationForm()
    
    return render(request, 'authenticate/register.html', {'form': form})

def students(request):
    submitted = False
    try:
        # Try to get the Student object associated with the current user
        student_instance = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        # If no Student object exists for the current user, create a new one
        student_instance = Student(user=request.user)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_instance)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = StudentForm(instance=student_instance)

    return render(request, 'authenticate/students.html', {'form': form, 'submitted': submitted})

def teacher(request):
    submitted = False
    try:
        # Try to get the Teacher object associated with the current user
        teacher_instance = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        # If no Teacher object exists for the current user, create a new one
        teacher_instance = Teacher(user=request.user)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher_instance)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = TeacherForm(instance=teacher_instance)

    return render(request, 'authenticate/teachers.html', {'form': form, 'submitted': submitted})

def display_students(request):
    students = Student.objects.all()  # Retrieve all students from the database
    return render(request, 'authenticate/table.html', {'students': students})

def display_marks(request):
    # Retrieve all Marks objects from the database
    marks_list = Marks.objects.all()
    
    # Pass the marks_list to the template for rendering
    return render(request, 'authenticate/table2.html', {'marks_list': marks_list})

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data['recipient']
            recipient = get_object_or_404(User, username=recipient_username)
            content = form.cleaned_data['content']

            message = Message.objects.create(
                sender=request.user,
                recipient=recipient,
                content=content
            )

            # Redirect or show a success message
            return redirect('conversation', recipient_username=recipient_username)
    else:
        form = MessageForm()

    return render(request, 'authenticate/send_message.html', {'form': form})

from django.db.models import Q

def conversation(request, recipient_username):
    recipient = get_object_or_404(User, username=recipient_username)
    messages = Message.objects.filter(
        Q(sender=request.user, recipient=recipient) | Q(sender=recipient, recipient=request.user)
    ).order_by('timestamp')

    form = MessageForm()
    return render(request, 'authenticate/conversation.html', {'messages': messages, 'recipient': recipient,'form':form})

