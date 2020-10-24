from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create',views.create,name='create'),
    path('<int:num>', views.index, name='index'),
    path('next2', views.index2, name='index2'),
    path('find', views.find, name='find'),
    path('message/', views.message, name='message'),
    path('message/<int:page>',views.message,name='message'),
]
