from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message
from .forms import RoomForm

import random


def loginPage(request):  # dont call it login - there will be conflict
    page = "login"

    if (
        request.user.is_authenticated
    ):  # redirect logged in user to home page if they try to go to login page
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password does not exist")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = UserCreationForm()  # django form for creating users

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # dont save to DB yet
            user.username = user.username.lower()
            user.save()
            user.login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Error occured during registration")

    context = {"form": form}

    return render(request, "base/login_register.html", context)


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )  # get all rooms in DB
    # icontains for partial queries - i at beginning makes it case - insensitive

    topic = Topic.objects.all()  # get all topics in DB
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {
        "rooms": rooms,
        "topics": topic,
        "room_count": room_count,
        "room_messages": room_messages,
    }
    return render(request, "base/home.html", context)


def room(request, pk):  # pk is primary key which is the the room number in the URL
    room = Room.objects.get(id=pk)  # get the room with the id of pk
    room_messages = room.message_set.all().order_by(
        "-created"
    )  # get all messages in room in order of creation
    participants = room.participants.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect("room", pk=room.id)

    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }
    return render(request, "base/room.html", context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {"user": user, "rooms": rooms, "room_messages": room_messages, "topics": topics}
    return render(request, "base/profile.html", context)


@login_required(login_url="login")  # if user is not logged in, redirect to login page
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)  # dont save to DB yet
            room.host = request.user
            room.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def updateRoom(request, pk):  # pk to know what item we're updating
    room = Room.objects.get(id=pk)
    form = RoomForm(
        instance=room
    )  # form will be prefilled with room that needs updating

    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        room.delete()  # simply remove room from DB
        return redirect("home")

    return render(request, "base/delete.html", {"obj": room})


@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        message.delete()  # simply remove message from DB
        if request.GET.get("from") == "home":
            return redirect("home")
        else:
            return redirect("room", pk=message.room.id)

    return render(request, "base/delete.html", {"obj": message})


def random_room(request):
    rooms = Room.objects.all()
    if rooms:
        room = random.choice(rooms)
        return redirect('room', pk=room.id)
    else:
        return redirect('home')