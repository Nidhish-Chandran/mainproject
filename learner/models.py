from django.db import models
# from django.utils import date
from datetime import date

class Logintable(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,null=True)
    
class StudentRegistration(models.Model):
    StudentId=models.CharField(max_length=100)
    StudentName=models.CharField(max_length=100)
    StudentClass=models.CharField(max_length=100)
    StudentContact=models.CharField(max_length=100)
    loginid=models.OneToOneField(Logintable,on_delete=models.CASCADE,related_name='student')

class userregistration(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    loginid=models.ForeignKey(Logintable,on_delete = models.CASCADE)

class mentors(models.Model):
    Name =models.CharField(max_length= 100)
    Gender = models.CharField(max_length=100)
    Qualification = models.CharField(max_length = 100)
    Expertes = models.CharField(max_length= 100)
    contact = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    loginid=models.ForeignKey(Logintable,on_delete = models.CASCADE)

class Company(models.Model):
    Name=models.CharField(max_length=40)
    Address=models.CharField(max_length=50)
    Contact=models.CharField(max_length=10)
    Reg_id=models.CharField(max_length=40)
    status = models.IntegerField(default=0)
    loginid=models.ForeignKey(Logintable, on_delete=models.CASCADE,null=True)

class Job(models.Model):
    Job_category = models.CharField(max_length=40)
    Job_name = models.CharField(max_length=40)
    Job_description = models.CharField(max_length=150)
    Job_qualification = models.CharField(max_length=100)
    Apply_before = models.DateField()
    Company_id = models.ForeignKey(Company,on_delete=models.CASCADE)

class Jobapplication(models.Model):
    Job_id = models.ForeignKey(Job,on_delete=models.CASCADE)
    loginid = models.ForeignKey(Logintable,on_delete = models.CASCADE)
    Resume = models.FileField(upload_to = 'Cadresume/' )
    status = models.IntegerField(default=0)
    Current_date = models.DateField(auto_now_add=True)

class mentorclass(models.Model):
    Mentor_id = models.ForeignKey(mentors,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Logintable,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    status = models.IntegerField(default = 0)
    cancel =models.IntegerField(default=0)
    url = models.URLField(null=True)







