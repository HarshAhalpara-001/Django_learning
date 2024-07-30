from django.shortcuts import render,HttpResponse

# Create your views here.
def movie(request):
    return render(request, 'movie/index.html', {'movie': 'Ironman'})
def about(request):
    return render(request, 'movie/about.html', {})