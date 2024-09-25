from django.shortcuts import render

from .models import Flights,Airport,Passenger
# Create your views here.
def flights(request):
    return render(request,'flight/flights.html',{
        'flights':Flights.objects.all()  
          })
    
def flight(request,flight_id):
    flight=Flights.objects.get(id=flight_id)
  
    return render(request,'flight/flight.html',{
        'flight':flight,
        'passengers': flight.passengers.all(),
        'non_passengers':Passenger.objects.exclude(flights=flight).all()
        
    })
    
def book(request,flight_id):
    if request.method == 'POST':
        flight=Flights.objects.get(id=flight_id)
        
    
    return render(request,flight/book.html,{
        'flight':flight,
        'non_passengers':Passenger.objects.exclude(flights=flight).all()
        
    })