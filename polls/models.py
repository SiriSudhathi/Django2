from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    rollNo = models.CharField(max_length=20,primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phoneNo = models.IntegerField(max_length=10)

class AcedamicInfo(models.Model):
	studentId = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	yearOfJoining = models.IntegerField(max_length=30)
	aggregate = models.IntegerField(max_length=30)
	upperSecondaryInstitution = models.CharField(max_length=70)
	upperSecondaryBoard = models.CharField(max_length=30)
	upperSecondaryPercentage = models.IntegerField(max_length=10)
	SecondaryPercentage = models.IntegerField(max_length=10)
	SecondaryInstitution = models.CharField(max_length=10)
	SecondaryBoard = models.CharField(max_length=10)

class AdditionalInfo(models.Model):
	studentId = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	coAcademicActivities = models.CharField(max_length=30)
	details = models.TextField(max_length=30)
	coCurriculars = models.CharField(max_length=30)
	hobbies = models.CharField(max_length=30)

class Notifications(models.Model):
	studentId = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	date = models.TextField()
	notification = models.CharField(max_length=30)


class Faculty(models.Model):
    faculty_suggestion = models.CharField(max_length = 200)
    student_refid = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)

class TPO(models.Model):
    drive_name = models.CharField(max_length = 20)
    TPO_notification = models.CharField(max_length = 200)
