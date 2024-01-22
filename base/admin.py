from django.contrib import admin

# Register your models here. aka whenever you make a class for database column you have to register it here, then makemigrations and then migrate

from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
