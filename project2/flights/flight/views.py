from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flights, Airport, Passenger

# Create your views here.
def flights(request):
    return render(request, 'flight/flights.html', {
        'flights': Flights.objects.all()  
    })
    
def flight(request, flight_id):
    flight = get_object_or_404(Flights, id=flight_id)
    
    return render(request, 'flight/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    flight = get_object_or_404(Flights, id=flight_id)
    
    if request.method == 'POST':
        passenger_id = request.POST.get('passenger')
        if passenger_id:
            passenger = get_object_or_404(Passenger, id=passenger_id)
            flight.passengers.add(passenger)
            return HttpResponseRedirect(reverse('flight', args=[flight_id]))
    
    return render(request, 'flight/book.html', {
        'flight': flight,
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })
