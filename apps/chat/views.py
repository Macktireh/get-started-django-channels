from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from apps.chat.models import Room


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })