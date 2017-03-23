from django.shortcuts import render,redirect
from django.http import HttpResponse
from polls.models import PersonInfo
from polls.forms import PersonInfoForm
from polls.models import AcedamicInfo
from polls.forms import AcedemicInfoForm
from polls.models import AdditionalInfo
from polls.forms import AdditionalInfoForm

# Create your views here.
def index(request):
    return HttpResponse("Welcome")
def base(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)
        if form.is_valid():
            PersonInfo = form.save(commit = False)
            PersonInfo.save()
            return redirect('academic')
    else:
        form = PersonInfoForm()
    return render(request,'polls/base.html',{'form':form})

def academic(request):
    if request.method == "POST":
        form = AcedemicInfoForm(request.POST)
        if form.is_valid():
            AcedamicInfo = form.save(commit = False)
            AcedamicInfo.save()
            return redirect('additional')
    else:
        form = AcedemicInfoForm()
    return render(request,'polls/academic.html',{'form':form})

def additional(request):
    if request.method == "POST":
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            AdditionalInfo = form.save(commit = False)
            AdditionalInfo.save()
            return redirect('success')
    else:
        form = AdditionalInfoForm()
    return render(request,'polls/additional.html',{'form':form})

def success(request):
    return HttpResponse("Successfully Updated")
