from django.urls import path, include

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("index/", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("register/", views.Register.as_view(), name="register"),
    path("<str:room_name>/", views.room, name="room"),
]
