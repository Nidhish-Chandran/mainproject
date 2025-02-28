from django import forms
from .models import *

class studentform(forms.ModelForm):

    class Meta:
        model = StudentRegistration
        fields = ['StudentId',  'StudentName','StudentClass','StudentContact']

class loginform(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Logintable
        fields = ['email','password']

class userform(forms.ModelForm):
    class Meta:
        model = userregistration
        fields =['Name','Gender','contact']

class logincheck(forms.Form):
        email = forms.CharField(max_length=100)
        password =forms.CharField(max_length=100)

class loginedit(forms.ModelForm):
     class Meta:
          model=Logintable
          fields=['email']

class mentorsform(forms.ModelForm):
     class Meta:
          model = mentors
          fields = ['Name','Gender','Qualification','Expertes','contact']

# Company's register form
class Companyform(forms.ModelForm):
    class Meta:
        model=Company
        fields=['Name','Address','Contact','Reg_id']

class Jobform(forms.ModelForm):
     class Meta:
          model = Job
          fields = ['Job_category','Job_name','Job_description','Job_qualification','Apply_before']

class Jobapplications(forms.ModelForm):
     class Meta:
          model = Jobapplication
          fields = ['Resume']

class MentorRequestForm(forms.ModelForm):
    class Meta:
        model = mentorclass
        fields = []




    

