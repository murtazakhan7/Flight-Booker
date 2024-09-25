from django.db import models

# Create your models here.

class Airport(models.Model):
    code=models.CharField(max_length=5)
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.code, self.city}"
    


class Flights(models.Model):
    
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='origin')
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE, related_name='destionation')
    duration=models.IntegerField()
    
    def __str__(self):
        return f"{self.id  , self.origin , self.destination, self.duration}"

class Passenger(models.Model):
    name=models.CharField(max_length=50)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")
    
    
    def __str__(self):
        return self.name