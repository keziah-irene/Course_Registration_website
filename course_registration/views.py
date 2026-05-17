from django.shortcuts import render, redirect
from .models import Courses, Students
from .forms import CourseRegistrationForm
from django.contrib import messages

def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'course_registration/course_list.html', {'courses': courses})

def register_course(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            if course.available_seats > 0:
                course.available_seats -=1
                course.save()
                form.save()
                return redirect('student_dashboard')
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration/register_course.html', {'form': form})

def student_dashboard(request):
    student = None
    student_course = None

    if request.method == 'GET' and 'student_id' in request.GET:
        student_id = request.GET.get('student_id')
        try:
            student = Students.objects.get(student_id=student_id)
            student_course = student.course
        except Students.DoesNotExist:
            messages.error(request, 'Student not found. Please check your Student ID.')
            student = None
    return render(request, 'course_registration/student_dashboard.html', 
                  {'student': student, 
                   'student_course': student_course})
        

