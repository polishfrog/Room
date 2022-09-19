from django.shortcuts import render, redirect
from django.views import View

from main.models import ConferenceRoom, RoomReservation

import datetime

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

class ModifyRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(pk=room_id)
        return render(request, 'modify_room.html', context={'room': room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(pk=room_id)
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projektor = request.POST.get('projector') == "on"

        if not name:
            return render(request, 'modify_room.html', context={'room': room,
                                                                'error': "Nie podano nazwy pokoju"})
        if capacity <= 0:
            return render(request, 'modify_room.html', context={'room': room,
                                                                'error': "Pojemność sali musi być dodatnia"})
        if name != room.name and ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'modify_room.html', context={'room': room,
                                                                'error': "Sala o podanej nazwie już istnieje!"})

        room.name = name
        room.capacity = capacity
        room.projector_availability = projektor
        room.save()
        return redirect("room-list")

class ReservationViev(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(pk=room_id)
        return render(request, 'reservation.html', context={'room': room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(pk=room_id)
        date = request.POST.get('reservation-date')
        comment = request.POST.get('comment')

        if RoomReservation.objects.filter(room_id=room, date=date):
            return render(request, 'reservation.html', context={'room': room,
                                                                'error': "Sala jest już zarezerwowana!"})

        if date < str(datetime.date.today()):
            return render(request, 'reservation.html', context={'room': room,
                                                                'error': "Niepoprawna data!"})
        RoomReservation.objects.create(room_id=room, date=date, comment=comment)
        return redirect('room-list')

