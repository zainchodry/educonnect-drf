from django.db import models
from accounts.models import User




class Course(models.Model):
    LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    level = models.CharField(max_length=20, choices=LEVELS)
    category = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="In hours")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title
    


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    completed = models.BooleanField(default = False)

    class Meta:
        unique_togather = ('student', 'course')


class Review(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


    class Meta:
        unique_togather = ('student', 'course')


        