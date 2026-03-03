from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from Admin.models import Student
from datetime import datetime


# Create your views here.

@login_required
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html',{'students': students})
def add_record(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')
        email = request.POST.get('email')
        date = request.POST.get('date')

        Student.objects.create(
            image = image,
            name=name,
            course=course,
            age=age,
            email=email,
            date=date)
        return redirect('index')
    return render(request, 'add_record.html')

def update_record(request, id):
    student = get_object_or_404(Student, id=id)  # use singular 'student'

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.age = int(request.POST.get('age', student.age))
        student.email = request.POST.get('email')
        # handle date safely
        date_input = request.POST.get('date')
        if date_input:
            student.date = datetime.strptime(date_input, '%Y-%m-%d').date()
        # handle file upload
        if request.FILES.get('image'):
            student.image = request.FILES.get('image')

        student.save()
        return redirect('index')

    # GET request: prefill form with student data
    return render(request, 'update_record.html', {'student': student})

def delete_record(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('index')  # change to your actual page name

    return redirect('index')
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists!')
            return redirect('sign_up')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password)

        login(request, user)
        return redirect('index')

    return render(request, 'sign_up.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,
                           'Invalid username and/or password.')
    return render(request, 'log_in.html')

def logout_view(request):
    logout(request)
    return redirect('log_in')

