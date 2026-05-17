from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    max_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Students(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    student_name = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        unique_together = ['student_id', 'course'] 
        
        
        
        # prevent multiple registrations; comes with a default error message
    

# str method - when we view a list of Teachers objects in the admin site, Django shows self.__str__() instead of the default like <Teachers object (1), Teachers object (2), ...>

