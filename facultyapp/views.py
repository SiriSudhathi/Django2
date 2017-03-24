from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm
from  facultyapp.models import Comment


def next(request):
    if request.method == "POST":
        form = ViewForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit = False)
            Comment.save()
            
            return redirect('success')
        
    else:
        form = ViewForm()
    return render(request, "frontpage.html", {'form': form})


def success(request):
    return HttpResponse('Your Notifications are updated successfully.')

def display(request):
         try:
             Student = Comment.objects.all()
         except Comment.DoesNotExist:
             raise Http404("Comment does not exist")
            
         return render(request, "display.html",{'Student': Student})
