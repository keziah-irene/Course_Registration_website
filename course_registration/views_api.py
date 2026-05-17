from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Courses, Students
from .serializers import CourseSerializer, StudentSerializer

@api_view(["GET"]) #decorator
def api_course_list(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_register_course(request):
    student_id = request.data.get('student_id')
    student_name = request.data.get('student_name')
    course_id = request.data.get('course_id')

    try:
        course = Courses.objects.get(id=course_id)
        if course.available_seats > 0:
            student, created = Students.objects.get_or_create(
                student_id=student_id,
                defaults={'student_name': student_name, 'course': course}
            )
            if not created:
                return Response({'error': 'student already registered for a course'}, status = status.HTTP_400_BAD_REQUEST)
            course.available_seats -= 1
            course.save()
            return Response({'message': 'registration successfull'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'no seats available'}, status= status.HTTP_400_BAD_REQUEST)
    except Courses.DoesNotExist:
        return Response({'error': 'given courseis not found'}, status= status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def api_student_dashboard(request):
    student_id = request.GET.get('student_id')
    try:
        student = Students.objects.get(student_id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Students.DoesNotExist:
        return Response({'error': 'student not found'}, status= status.HTTP_404_NOT_FOUND)
