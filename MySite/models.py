from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=250)
    code = models.PositiveIntegerField()
    department = models.CharField(max_length=250, choices=[
        ('COMPUTER SCIENCES', 'COMPUTER SCIENCES'),
        ('BIOLOGICAL SCIENCES', 'BIOLOGICAL SCIENCES'),
        ('CHEMICAL SCIENCES', 'CHEMICAL SCIENCES'),
        ('MANAGEMENT SCIENCES', 'MANAGEMENT SCIENCES'),
        ('MASS COMMUNICATION', 'MASS COMMUNICATION'),
        ('CRIMINOLOGY', 'CRIMINOLOGY'),
        ('GENERAL STUDIES', 'GENERAL STUDIES'),
    ])
    lecturer = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    matric_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.matric_no


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mode_of_teaching = models.PositiveIntegerField()
    communication = models.PositiveIntegerField()
    relationship = models.PositiveIntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.course


class Ranking(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.course

    def calculate_point(self):
        ratings = Rating.objects.filter(course=self.course)
        avg_points = 0
        for rat in ratings:
            avg_points += (rat.mode_of_teaching + rat.communication + rat.relationship) / 3

        self.points = avg_points / len(ratings)
        self.save()
