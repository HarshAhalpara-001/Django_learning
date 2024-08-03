from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Link
# Create your views here.
def home(request):
    context={
        'link' : Link.objects.all()
    }
    return render(request, 'link/index.html',context)
def root_link(request, link_slug):
    link= get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)
def add_link(request):
    name=request.POST.get('name')
    url=request.POST.get('url')
    x=Link.objects.filter(url=url)
    if not x:
        Link.objects.create(name=name,url=url)
    else:
        pass
    context={
        'link' : Link.objects.all()
    }
    return render(request, 'link/index.html',context)

            