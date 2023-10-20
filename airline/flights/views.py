from django.shortcuts import render
from .models import Flight, Airport

# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{
        'flights' : Flight.objects.all()
    })

def flight(request, flight_id):
    #first get the flight whose primary key is flight_id
    flight= Flight.objects.get(pk=flight_id)
    #then pass in the flight to a render request for flight.html
    return render(request, 'flights/flight.html',{
        'flight': flight
    })
