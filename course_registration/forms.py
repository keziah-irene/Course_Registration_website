from django import forms
from .models import Students, Courses

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_id', 'student_name', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # override to customize the default behavior of init method
        self.fields['course'].queryset = Courses.objects.filter(available_seats__gt=0)



