"""Room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', views.AddRoomView.as_view(), name='add-room'),
    path('', views.RoomListView.as_view(), name='room-list'),
    path('room/delete/<int:room_id>/', views.DeleteRoomView.as_view(), name='delete-room'),
    path('room/modify/<int:room_id>/', views.ModifyRoomView.as_view(), name='modify-room'),
    path('room/reserve/<int:room_id>/', views.ReservationViev.as_view(), name='reserve-room'),
    path('room/<int:room_id>/', views.RoomDetailsView.as_view(), name='room'),
    path('search/', views.SearchView.as_view(), name='room-list'),
]
