from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import ViewForm,Acad_details,Add_details
from  student.models import PersonInfo,AcedamicInfo,AdditionalInfo



# Create your views here.

def success(request):
try:
student_details = PersonInfo.objects.all()
acadamic_details = AcedamicInfo.objects.all()
additional_details = AdditionalInfo.objects.all()
except PersonInfo.DoesNotExist:
raise Http404("StudentPersonalInfo does not exist")
return render(request, 'success.html', {'student_details': student_details,'acedamic_details': acedamic_details,'additional_details': additional_details})


