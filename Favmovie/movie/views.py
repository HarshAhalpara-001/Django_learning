from django.shortcuts import render,HttpResponse

# Create your views here.
def movie(request):
    return render(request, 'movie/index.html', {
        'movie':
        ['ironman','spiderman','captain america','hulk']
    })
def about(request):
    return render(request, 'movie/about.html', {})