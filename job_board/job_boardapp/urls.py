from django.urls import path
from .views import home,jobno
urlpatterns = [
    path('', home),
    path('jobno./<int:k>',jobno ,name='jobno' ),
]