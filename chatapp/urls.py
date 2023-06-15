
from django.urls import path,include
from . import views



urlpatterns = [
   
    path('',views.index,name='index'),
    path('create-group/',views.create_chatroom,name='create-group'),
    path('register/',views.register , name ='register'),
    path('login/',views.user_login , name ='user_login'),
    path('logout/',views.user_logout , name ='user_logout'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
]
