from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("clear-chat/", views.clear_chat, name="clear_chat")
]