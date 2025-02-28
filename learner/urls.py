from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index,name='index'),                                                  # index page
    path('adminform',views.adminform,name='adminform'),                                 # admin page
    path('login',views.login_view,name='login'),                                        # loginpage
    path('adminheader',views.adminheader,name='adminheader'),                           # admin with only header
    path('regstudent',views.registerstudent, name='regstudent'),                        # page for student registration
    path('userregister',views.registeruser,name='userregister'),                        # page for user register
    path('mentorreg',views.mentorregister,name='mentorreg'),                            # page for mentor register
    path('login2',views.login_view,name='login2'),                                      # page for login
    path('userindex',views.userindex,name='userindex'),                                 # student index page
    path('studindex',views.studindex,name='studindex'),                                 # student index page
    path('studenttableview',views.studenttablesload,name='studenttablesview'),          # student_table
    path('usertableview',views.usertableload,name='usertableview'),                     # user_table
    path('editstud',views.student_edit,name='editstud'),                                # student_edit
    path('edituser',views.user_edit,name='edituser'),                                   # user_edit
    path('mentorindex',views.mentorindex,name='mentorindex'),                           # mentor index page 
    path('mentorreg',views.mentorregister,name='mentorreg'),                            # metor registration
    path('editmentor',views.mentor_edit,name='editmentor'),                             # metor profile page
    path('mentortable',views. mentortableview,name='mentortable'),                      # admin view of mentors list for approval
    path('mentor_reject/<int:id>/',views.mentor_reject,name='mentor_reject'),           
    path('mentor_approve/<int:id>/',views.mentor_approve,name='mentor_approve'),
    path('companyindex',views.companyindex,name='companyindex'),                        # company index page
    path('company_register',views.Company_register,name='company_register'),            # company register page
    path('companyedit',views.CompanyEdit,name='companyedit'),                           # company profile page
    path('companytable',views.companytableview,name='companytable'),                    # admin view of company list for approval
    path('company_reject/<int:id>/',views.company_reject,name='company_reject'),
    path('company_approve/<int:id>/',views.company_approve,name='company_approve'),
    path('job_upload',views.Job_Upload,name='job_upload'),                              # page for company to load job
    path('job_edit/<int:id>/',views.Job_Edit,name='job_edit'),                          # page for company to edit it's apploaded job details
    path('job_apply/<int:id>/',views.Jobapply,name='job_apply'),                        # page for user to apply for the job posted by companyes
    path('job_company',views.JobCompanyView,name='job_company'),                        # page for company to view their uploaded job
    path('Jobapplicationview',views.Jobapplicationview,name='Jobapplicationview'),      # page for company to show the applicants
    path('Job_approve/<int:id>/',views.Job_approve,name='Job_approve'),
    path('Job_reject/<int:id>/',views.Job_reject,name='Job_reject'),
    path('job_view',views.Job_View,name='job_view'),                                    #
    path('job_status',views.Job_status,name='job_status'),
    path('logout/',views.logout_user,name='logout'),
    path('videoclass/<int:id>/',views.videoconference,name='videoclass'),
    path('mentorslist',views.mentorslist,name="mentorslist"),
    path('mentorrequest/<int:id>/',views.mentorrequest,name='mentorrequest'),
    path('students_applied_for_mentorclass',views.students_applied_for_mentorclass,name='students_applied_for_mentorclass'),      # page for mentor to show the students list
    # path('class_approve/<int:id>/',views.class_approve,name='class_approve'),
    # path('class_reject/<int:id>/',views.class_reject,name='class_reject'),
    path('class_status',views.class_status,name='class_status'),
    path('studentapprove/<int:id>/',views.Student_approve_by_mentor,name='studentapprove'),
    path('studentreject/<int:id>/',views.Student_reject_by_mentor,name='studentreject'),
    path('cancel_pending_class/<int:id>/',views.cancel_pending_class,name='cancel_pending_class'),
    path('save_url/<int:id>/', views.save_url, name='save_url'),


    #  path('enrollstudent/<int:id>/',views.enrollstudent,name='enrollstudent'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)