from django.shortcuts import render
from .models import Chatroom,ChatMessage
from django.http import HttpResponse

# Create your views here.

def index(request):
    chatrooms = Chatroom.objects.all()
    
    return render (request ,'chatapp/index.html',{'chatrooms':chatrooms})


def chatroom(requset,slug):
    chatroom = Chatroom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room = chatroom)[0:10]
    return render (requset , "chatapp/room.html",{'chatroom':chatroom ,'messages':messages})


def create_group(request):
    return render(request , 'chatapp/create_group.html' , {})