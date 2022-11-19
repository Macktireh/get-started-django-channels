from typing import Any, Sequence, Union
from django.contrib import admin

from apps.chat.models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str,  Any]] = ['name']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str,  Any]]  = ['user', 'room', 'content', 'timestamp']
