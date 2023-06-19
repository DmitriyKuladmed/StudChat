import json

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.views import View
from django.contrib.auth import login as auth_login

from .forms import UserCreationForm
from .models import User

admin.site.register(User)


def info(request):
    return render(request, "chat/home.html")


def register(request):
    return render(request, "chat/register.html")


def login(request):
    return render(request, "chat/login.html")


def home(request):
    return render(request, "chat/home.html")


def index(request):
    return render(request, "chat/index.html")

@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {
        "room_name": room_name,
    })


class Register(View):

    template_name = "registration/register.html"

    def get(self, request):
        context = {
            "form": UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('first')
        else:
            return render(request, self.template_name, {
                'form': form
            })

