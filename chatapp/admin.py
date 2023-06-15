from django.contrib import admin
from .models import Chatroom,ChatMessage,UserProfile

# Register your models here.
admin.site.register(Chatroom)
admin.site.register(ChatMessage)
admin.site.register(UserProfile)