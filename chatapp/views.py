from django.shortcuts import render,redirect
from .models import Chatroom,ChatMessage
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from .models import Chatroom
from django.db import IntegrityError
from .forms import ChatroomForm,UserForm ,UserProfileForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ,logout


def index(request):
    chatrooms = Chatroom.objects.all()
    
    return render (request ,'chatapp/index.html',{'chatrooms':chatrooms})

@login_required
def chatroom(requset,slug):
    chatroom = Chatroom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room = chatroom)[0:10]
    return render (requset , "chatapp/room.html",{'chatroom':chatroom ,'messages':messages})



    

@login_required
def create_chatroom(request):
    if request.method == 'POST':
        form = ChatroomForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, 'Chatroom created successfully!')
            return redirect('index')  
        else:
            messages.error(request, 'Chatroom creation failed. Nick-Name Alreasy Exist.')
    else:
        form = ChatroomForm()

    return render(request, 'chatapp/create_group.html', {'form': form})

##########################################################################################################################
#############################################################################################
###################################################################
##########################################
####################

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Create a user object but don't save it yet
            user = user_form.save(commit=False)
            
            # Set the password using set_password() method
            password = user_form.cleaned_data['password']
            user.set_password(password)

            # Save the user object
            user.save()

            # Proceed with saving the profile form and other data
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()

            registered = True
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }
    
    return render(request, 'chatapp/register.html', context)




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the appropriate URL name or path
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'chatapp/login.html')


def user_logout(request):
    logout(request)
    # Redirect to the desired page after logout
    return redirect('index')