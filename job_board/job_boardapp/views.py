from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import JobPosting
# Create your views here.
def home(request):
    active = JobPosting.objects.filter(is_active=True)
    context={
        'job' : active
    }
    return render(request, 'job_boardapp/index.html',context)
def jobno(request,k):
    job=get_object_or_404(JobPosting,id=k)
    context={
        'job' : job
    }
    return render(request, 'job_boardapp/detail.html',context)
