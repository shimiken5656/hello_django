from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('next2', views.index2, name='index2'),
    path('find', views.find, name='find'),
]
