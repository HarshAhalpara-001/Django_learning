from django.shortcuts import render,HttpResponse,get_list_or_404
from .models import JobPosting
# Create your views here.
def home(request):
    active = JobPosting.objects.filter(is_active=True)
    context={
        'job' : active
    }
    return render(request, 'job_boardapp/index.html',context)
def jobno(request,k):
    return HttpResponse(f" the title of job id is :{JobPosting.objects.get(id=k).title}")
