from django.urls import path
from . import views

urlpatterns = [
    path('room/', views.RoomView.as_view())
]
