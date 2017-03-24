from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = (
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('tpo', 'TPO'),
)

DEGREE = (
    ('ece', 'ECE'),
    ('cse', 'CSE'),
    ('mech', 'MECHANICAL'),
)

class User(AbstractUser):
    mobile = models.CharField(max_length=100, default='')
    address = models.TextField()
    userRole = models.CharField(choices=USER_ROLES, max_length=50)

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    rollNo = models.CharField(max_length=20,primary_key = True)
    department = models.CharField(choices=DEGREE, max_length=30)
    activities = models.CharField(max_length=300)
    achievements = models.TextField()
    hobbies = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class AcademicInfo(models.Model):

    student = models.ForeignKey(StudentProfile,related_name="student_acinfo")
    yearOfPassing = models.IntegerField()
    aggregate = models.IntegerField()
    institution = models.CharField(max_length=70)
    board = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)

    def __str__(self):
        return self.student.user.username

class JobNotifications(models.Model):
    title = models.CharField(max_length=30)
    notification = models.TextField()

class Suggestions(models.Model):
    student = models.ForeignKey(User, related_name="sgstn_student")
    notification = models.TextField()
    faculty = models.ForeignKey(User, related_name="sgstn_faculty")



# class Faculty(models.Model):
#     faculty_suggestion = models.CharField(max_length = 200)
#     student_refid = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
