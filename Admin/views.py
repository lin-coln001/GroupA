from django.shortcuts import render, redirect, get_object_or_404

from Admin.models import Student
from datetime import datetime


# Create your views here.
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
