from django.shortcuts import render, redirect
from django.views import View

from main.models import ConferenceRoom


# Create your views here.


class AddRoomView(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projektor = request.POST.get('projektor') == "on"

        if not name:
            return render(request, 'add_room.html', context={'error': "Nie podano nazwy sali"})
        elif capacity <= 0:
            return render(request, 'add_room.html', context={'error': 'Pojemność sali musi być dodatnia'})
        elif ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'add_room.html', context={'error': 'Sala o podanej nazwie istnieje'})

        ConferenceRoom.objects.create(name=name, capacity=capacity, projector_availability=projektor)
        return redirect('room-list')

class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, 'rooms.html', context={'rooms': rooms})

class DeleteRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(pk=room_id)
        room.delete()
        return redirect('room-list')