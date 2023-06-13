
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('create-group/',views.create_group,name='create-group'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
]
