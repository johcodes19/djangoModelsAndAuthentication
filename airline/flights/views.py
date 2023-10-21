from django.shortcuts import render
from .models import Flight, Airport, passenger

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
        'flight': flight,
        'passengers':flight.passengers.all() 
        #we are saying flight.passengers because passengers is the related name in the many to many relationship with flight class
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(id=flight_id)
        pasenger= passenger.objects.get(pk=int(request.POST['passenger']))
        pasenger.flights.add(flight)