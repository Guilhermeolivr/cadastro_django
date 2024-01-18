from django.shortcuts import render
from .models import Message, Room

def home(request):
    messages = Message.objects.all()
    rooms = Room.objects.all()
    return render(request,'chat/home.html',{
        'room' : rooms,
        'messages' : messages})