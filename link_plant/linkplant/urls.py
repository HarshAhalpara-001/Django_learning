from django.urls import path, include
from .views import LinkListView , LinkCreateView
urlpatterns = [
    path('',LinkListView.as_view(), name='link-list'),
    path('link/create',LinkCreateView.as_view(), name='link-create'),

]
