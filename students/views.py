from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, StudentProfile, AcademicInfo, JobNotifications, Suggestions
from .forms import StudentRegistrationForm, StudentProfileForm, AcademicInfoForm, JobNotificationsForm
from django.shortcuts import get_object_or_404, render

# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        print(request.user.userRole)
        if request.user.userRole =="student":
            return HttpResponseRedirect("/student/dashboard/")
        if request.user.userRole == "faculty":
            return HttpResponseRedirect("/faculty/dashboard/")
        if request.user.userRole == "tpo":
            return HttpResponseRedirect("/tpo/dashboard/")

def student_dashboard(request):
    suggestions = Suggestions.objects.filter(student=request.user)
    notifications = JobNotifications.objects.all()
    return render(request, 'student_dashboard.html', {"student": request.user, "suggestions": suggestions, "notifications":notifications})


def student_profile(request, pk):
    student = get_object_or_404(User, pk=pk, userRole="student" )
    education_details = AcademicInfo.objects.filter(student=student.student)
    return render(request, 'student_profile_view.html', {"student": student, "education_details": education_details})

def student_message(request, pk):
    student = get_object_or_404(User, pk=pk, userRole="student" )
    if request.method == "POST":
        Suggestions.objects.create(student=student, notification=request.POST['message'], faculty=request.user)
    suggestions = Suggestions.objects.filter(student=student)
    return render(request, 'add_message_to_student.html', {"student": student, "suggestions":suggestions})



def faculty_dashboard(request):
    students = User.objects.filter(userRole = "student")
    print(students.count())
    notifications = JobNotifications.objects.all()
    return render(request, 'faculty_dashboard.html', {'students': students,'notifications': notifications})

def tpo_dashboard(request):
    if request.method == "POST":
        form = JobNotificationsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/tpo/dashboard/')
    notifications = JobNotifications.objects.all()
    form = JobNotificationsForm()
    return render(request, 'add_notification.html', {"form": form, "notifications": notifications})

#
# def academic(request):
#     if request.method == "POST":
#         form = AcedemicInfoForm(request.POST)
#         if form.is_valid():
#             AcedamicInfo = form.save(commit = False)
#             AcedamicInfo.save()
#             return redirect('additional')
#     else:
#         form = AcedemicInfoForm()
#     return render(request,'polls/academic.html',{'form':form})
#
# def additional(request):
#     if request.method == "POST":
#         form = AdditionalInfoForm(request.POST)
#         if form.is_valid():
#             AdditionalInfo = form.save(commit = False)
#             AdditionalInfo.save()
#             return redirect('success')
#     else:
#         form = AdditionalInfoForm()
#     return render(request,'polls/additional.html',{'form':form})
#
# def success(request):
#     return HttpResponse("Successfully Updated")
