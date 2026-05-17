from django.urls import path
from . import views, views_api

urlpatterns = [
    # for template rendering
    # http://127.0.0.1:8000/admin/ - Django admin site
    path('', views.course_list, name='course_list'),
    path('register_course/', views.register_course, name='register_course'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),

    # for API testing
    path('api/courses/', views_api.api_course_list, name='api-courses'),
    path('api/register/', views_api.api_register_course, name='api-register'),
    path('api/student-dashboard/', views_api.api_student_dashboard, name='api-dashboard'),
]

