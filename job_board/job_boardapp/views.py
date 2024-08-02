from django.shortcuts import render,HttpResponse
from .models import JobPosting
# Create your views here.
def home(request):
    active = JobPosting.objects.filter(is_active=True)
    context={
        'job' : active
    }
    return render(request, 'job_boardapp/index.html',context)
