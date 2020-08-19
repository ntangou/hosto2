from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='indexservice'),
    path('personnels', views.personnel, name='indexpersonnel'),
]
