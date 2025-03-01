import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.utils import *

# Create your views here.
def index(request):
    return render(request,'index.html')

# user index fn
def userindex(request):
    return render(request,'userindex.html')

# student index fn
def studindex(request):
    return render(request,'studentindex.html')


def adminform(request):
    return render(request,'adminform.html')

def login(request):
    return render(request,'login.html')

def adminheader(request):
    return render(request,'adminheader.html')


def mentorindex(request):
    return render(request,'mentorindex.html')

# register for students
def registerstudent(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        logform = loginform(request.POST)
        if(form.is_valid() and logform.is_valid()):
            user = logform.save(commit = False)
            user.usertype='student'
            user.save()
            studentdetails = form.save(commit = False)
            studentdetails.loginid = user
            studentdetails.save()
            messages.success(request ,"student registered")
            return redirect('login')
    else:
        form = studentform()
        logform = loginform()
    return render(request,'registration.html',{'form':form,'logform' : logform})


#registrtion for common user
def registeruser(request):
    if request.method =='POST':
        form = userform(request.POST)
        logform=loginform(request.POST)
        if(form.is_valid() and logform.is_valid()):
            user=logform.save(commit=False)
            user.usertype='common_user'
            user.save()
            userdetails = form.save(commit = False)
            userdetails.loginid=user
            userdetails.save()
            messages.success(request,'user registered')
            return redirect('login')
    else:
        form=userform()
        logform=loginform()
    return render(request,'registration.html',{'form':form,'logform':logform})


#register for mentors

def mentorregister(request):
    if request.method == 'POST':
        form = mentorsform(request.POST)
        logform =loginform(request.POST)
        if form.is_valid() and logform.is_valid():
            user = logform.save(commit=False)
            user.usertype = 'mentors'
            user.save()
            user_details = form.save(commit=False)
            user_details.loginid=user
            user_details.save()
            messages.success(request,'user registered')
            return redirect('login')
    else:
        form=mentorsform()
        logform=loginform()
    return render(request,'registration.html',{'form':form,'logform':logform})


#login code for all users
def login_view(request):
    if request.method =='POST':
        form = logincheck(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Logintable.objects.get(email=email)
                if user.password == password:
                    if user.usertype =='student':
                        request.session['student_id']=user.id   #     OR   request.session.get('session_id')
                        return redirect('studindex')
                    elif user.usertype=='common_user':
                         request.session['user_id']=user.id
                         return redirect('userindex')
                    if user.usertype == 'mentors' :
                         mentor = mentors.objects.get(loginid=user.id)
                         if mentor.status == 1:
                                request.session['mentor_id']=user.id
                                return redirect('mentorindex')
                    if user.usertype =='Company':
                         company = Company.objects.get(loginid=user.id)
                         if company.status == 1:
                                request.session['company_id']=user.id   #     OR   request.session.get('session_id')
                                return redirect('companyindex')
                else:
                    messages.error(request,'Invalid password')
            except Logintable.DoesNotExist:
                messages.error(request, 'user does not exist')
    else:
        form = logincheck()
    return render(request,'login.html',{'form':form})
        

#tables studentview

def studenttablesload(request):
    a = StudentRegistration.objects.all()
    return render(request,'adminstudentview.html',{'datas':a})

#tables userview
def mentorslist(request):
    id = request.session['student_id']
    d =mentorclass.objects.filter(student_id=id)
    user=get_object_or_404(Logintable,id=id)
    a=mentors.objects.all()
    return render(request,'mentorslist.html',{'datas':a,'id':user,'details':d})

# def mentorrequest(request,id):
#     mentor=get_object_or_404(mentors,id=id)
#     if request.method=='POST':
#         form= MentorRequestForm(request.POST)
#         if (form.is_valid()):
#             id1=request.session['student_id']
#             student = get_object_or_404(Logintable,id=id1)
#             class_req=form.save(commit=False)
#             class_req.Mentor_id=mentor
#             class_req.student_id=student
#             class_req.status=1
#             class_req.save()
#             messages.success(request,'you have successfully requested to join this class ')
#             return redirect('studindex')
#     else:
#         form=MentorRequestForm()
#     return render(request,'liveclass.html',{'form':form})
def mentorrequest(request, id):
    mentor = get_object_or_404(mentors, id=id)
    id1 = request.session.get('student_id')
    student = get_object_or_404(Logintable, id=id1)

    # Check if the student has already applied for this mentor
    existing_request = mentorclass.objects.filter(Mentor_id=mentor, student_id=student).first()
    
    if existing_request:
        messages.warning(request, "You have already applied for this class.")
        return render(request, 'liveclass.html', {'already_applied': True})  # Redirect with warning
    if request.method == 'POST':
        form = MentorRequestForm(request.POST)
        if form.is_valid():
            class_req = form.save(commit=False)
            class_req.Mentor_id = mentor
            class_req.student_id = student
            # class_req.status = 0  # Set the status to applied
            class_req.save()
            messages.success(request, "You have successfully requested to join this class.")
            return redirect('studindex')
    else:
        form = MentorRequestForm()

    return render(request, 'liveclass.html', {'form': form, 'already_applied': False})



def usertableload(request):
    a = userregistration.objects.all()
    return render(request,'adminusersview.html',{'datas':a})


#tables mentorview

def mentortableview(request):
    a = mentors.objects.all()
    return render(request,'adminmentor.html',{'datas':a})


def student_edit(request):
    id = request.session.get('student_id')
    print(id)
    users=get_object_or_404(Logintable,id=id)
    print(users)
    student = get_object_or_404(StudentRegistration,loginid=users)
    print(student)
    if request.method =='POST':
        form = studentform(request.POST,instance=student)
        login = loginedit(request.POST,instance=users)
        if form.is_valid() and login.is_valid():
            form.save()
            login.save()
            messages.success(request,'STUDENT DETAILS EDITED SUCCESSFULLY')
            return redirect('studindex')
    else:
        form=studentform(instance=student)
        login=loginedit(instance=users)
    return render(request,'edit.html',{'form':form,'login':login})


def user_edit(request):
    id = request.session.get('user_id')
    users=get_object_or_404(Logintable,id=id)
    common_user = get_object_or_404(userregistration,loginid=users)
    if request.method =='POST':
        form = userform(request.POST,instance=common_user)
        login = loginedit(request.POST,instance=users)
        if form.is_valid() and login.is_valid():
            form.save()
            login.save()
            messages.success(request,'USER DETAILS EDITED SUCCESSFULLY')
            return redirect('userindex')
    else:
        form=userform(instance=common_user)
        login=loginedit(instance=users)
    return render(request,'edit.html',{'form':form,'login':login})

def mentor_edit(request):
    id= request.session['mentor_id']
    users = get_object_or_404(Logintable,id=id) 
    mentor= get_object_or_404(mentors,loginid=id) 
    if request.method == 'POST':
        form = mentorsform(request.POST,instance =mentor)
        login1form=loginedit(request.POST,instance=users)
        if form.is_valid() and login1form.is_valid():
            form.save()
            login1form.save()
            messages.success(request,'Mentord details updated successfully!!!')
            return redirect('mentorindex')
    else:
        form =mentorsform(instance=mentor)
        login1form=loginedit(instance=users)
    return render(request,'edit.html',{'form':form,'login':login1form})

def mentor_reject(request,id):
    mentor = get_object_or_404(mentors,id=id)
    # logindetails = get_object_or_404(Logintable,id=mentor.id)
    mentor.status=2
    mentor.save()
    # messages.success(request,'Mentor Deleted successfully!!!')
    return redirect('mentortable')

def mentor_approve(request,id):
    mentor = get_object_or_404(mentors,id=id)
    mentor.status=1
    mentor.save()
    return redirect('mentortable')

# company code


def companyindex(request):
    return render(request,'companyindex.html')                  #company index page 

def Company_register(request):                
        if request.method=='POST':
            form= Companyform(request.POST)
            logform=loginform(request.POST)                                             #company register page
            if (form.is_valid() and  logform.is_valid()):
                user=logform.save(commit=False)
                user.usertype='Company'
                user.save()
                b=form.save(commit=False)
                b.loginid=user
                b.save()
                messages.success(request,'Company registered')
                return redirect('login')
        else:
            form=Companyform()
            logform=loginform()
        return render(request,'registration.html',{'form':form,'logform':logform})

def CompanyEdit(request):
    id= request.session['company_id']
    users = get_object_or_404(Logintable,id=id)                                     #company profile edit
    company = get_object_or_404(Company,loginid=id) 
    if request.method == 'POST':
        form = Companyform(request.POST,instance =company)
        logform=loginedit(request.POST,instance=users)
        if form.is_valid() and logform.is_valid():
            form.save()
            logform.save()
            messages.success(request,'Company details updated successfully!!!')
            return redirect('mentorindexpage')
    else:
        form = Companyform(instance=company)
        logform=loginedit(instance=users)
        return render(request,'edit.html',{'form':form,'login':logform})
    

def companytableview(request):                                                          #company table view by admin
    a = Company.objects.all()
    return render(request,'admincompany.html',{'datas':a})

def company_approve(request,id):
    companydetails = get_object_or_404(Company,id=id)                                       #company approved by admin
    companydetails.status=1
    companydetails.save()
    return redirect('companytable')

def company_reject(request,id):
    companydetails = get_object_or_404(Company,id=id)                                           #company rejected by company
    companydetails.status=2
    companydetails.save()
    return redirect('companytable')



# job management in Skillnest



def Job_Upload(request):                
        if request.method == 'POST':                                    #job upload by company
            form= Jobform(request.POST)
            if (form.is_valid()):
                id = request.session['company_id']
                users = get_object_or_404(Logintable,id=id) 
                company = get_object_or_404(Company,loginid=users) 
                job_des = form.save(commit = False)
                job_des.Company_id = company
                job_des.save()
                messages.success(request,'Job Uploaded....!')
                return redirect('job_upload')
        else:
            form = Jobform()
        return render(request,'job_upload.html',{'form':form})



def JobCompanyView(request):                                                        #job viewed by the company 
     id= request.session['company_id']
     a=get_object_or_404(Company,loginid=id)
     b=Job.objects.filter(Company_id=a)
     return render(request,'jobcompanyview.html',{'datas':b})

def Job_Edit(request,id):                                                           #job edit by the company
     jobdes =  get_object_or_404(Job,id=id)
     if request.method == 'POST':
        form = Jobform(request.POST,instance =jobdes)
        if form.is_valid():
            form.save()
            messages.success(request,'Job details updated successfully!!!')
            return redirect('job_company')
     else:
        form = Jobform(instance=jobdes)
        return render(request,'edit.html',{'form':form})
     
def Jobapply(request,id):
    jobdes =  get_object_or_404(Job,id=id)                                  #job apply by users
    if request.method == 'POST':
        form= Jobapplications(request.POST, request.FILES)
        if (form.is_valid()):
            id = request.session['student_id']
            users = get_object_or_404(Logintable,id=id) 
            job_App = form.save(commit = False)
            job_App.Job_id = jobdes
            job_App.loginid = users
            job_App.save()
            messages.success(request,'Job Applied....!')
            return redirect('job_view')
    else:
        form = Jobapplications()
    return render(request,'jobapply.html',{'form':form})


def Jobapplicationview(request):                                                #job applicant view by company
    a = Jobapplication.objects.all()
    return render(request,'jobapplicationcompany.html',{'datas':a})
     

def Job_approve(request,id):                                                #job applicant request approved by company
    applicant = get_object_or_404(Jobapplication,id=id)
    applicant.status=1
    applicant.save()
    return redirect('Jobapplicationview')

def Job_reject(request,id):                                                 #job applicant request rejected by company
    applicant = get_object_or_404(Jobapplication,id=id)
    applicant.status=2
    applicant.save()
    return redirect('Jobapplicationview')


def Job_View(request):                                                       #job viewed by user               
    a = Job.objects.all()
    return render(request,'job_view.html',{'datas':a})


def Job_status(request):
    id = request.session['user_id']                                                         #job application status
    user = get_object_or_404(Logintable,id=id)
    a = Jobapplication.objects.all()
    return render(request,'jobstatus.html',{'datas':a,'id':user})

#user logout for all type of user

def logout_user(request):
    request.session.flush()
    return redirect('login')







#student details mentor view

def students_applied_for_mentorclass(request):
    mentor_id = request.session['mentor_id']
    mentor = mentors.objects.get(loginid=mentor_id)
    applied_students = mentorclass.objects.filter(Mentor_id=mentor).select_related('student_id__student')

    return render(request, 'mentorstudentlist.html', {'students': applied_students})


# student requested for class approved or rejected by  mentor

def Student_approve_by_mentor(request,id):
    student1 = get_object_or_404(mentorclass,id=id)
    student1.status=1
    student1.save()
    return redirect('students_applied_for_mentorclass')


def Student_reject_by_mentor(request,id):
    student1 = get_object_or_404(mentorclass,id=id)
    student1.status=2
    student1.save()
    return redirect('students_applied_for_mentorclass')

#user seeing the mentors in the app


def class_status(request):
    id = request.session['student_id']
    user = get_object_or_404(Logintable,id=id)
    a = mentorclass.objects.all()
    return render(request,'studentclassstatus.html',{'datas':a,'id':user})

#student cancel class pending request

def cancel_pending_class(request,id):
    student = get_object_or_404(mentorclass,id=id)
    student.delete()
    return redirect('class_status')
    

#video coference code 

def videoconference(request,id):
    student = get_object_or_404(mentorclass,id=id)
    return render(request,'videoconference.html',{'id' :student})

# def enrollstudent(request,id):
#     stud = get_object_or_404(mentorclass,id=id)

# @csrf_exempt
# def save_url(request,id):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         url =data.get('url')

#         if url:
#             student = get_object_or_404(mentorclass,id=id)
#             student.url = url
#             student.save()
            
#             return JsonResponse({'success': True, 'message': 'URL saved successfully'})

#         return JsonResponse({'success': False, 'message': 'No URL provided'}, status=400)

#     return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)



@csrf_exempt
def save_url(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        if url:
            try:
                # Check if mentorclass with the given ID exists
                student = get_object_or_404(mentorclass, id=id)
                student.url = url
                student.save()
                
                print(f"URL saved successfully for mentorclass with id {id}. URL: {url}")
                return JsonResponse({'success': True, 'message': 'URL saved successfully'})

            except Exception as e:
                print(f"Error saving URL: {e}")
                return JsonResponse({'success': False, 'message': 'Error saving URL'}, status=500)

        return JsonResponse({'success': False, 'message': 'No URL provided'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

