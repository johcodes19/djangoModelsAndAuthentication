from django.db import models

# Create your models here.
#class Flight(models.Model):
    #this class called flight will have all the properties a flight should have
    #origin= models.CharField(max_length=64)
    #destination= models.CharField(max_length=64)
    #duration= models.IntegerField()
    #from here I will create migrations to tell django to take into account the changes I have made in my models and put them in a database
    #to do that, you go to the terminal and type python manage.py makemigrations
    #then python manage.py migrate
    #then python manage.py shell to enter the shell
'''
    in the shell, run - from flights.models import Flight...... where flights is the name of the app and the other Flight is the class
    from there you can add values to the Flight like this......
    f= Flight(origin='New York', destination='London' , duration=415)
    f.save()
    to return a string representation of the Flight object, we do this,,,,
     def __str__(self) :
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes"
'''
#I want to create a relationship between a flight and an airport, where the airport will have the name of the city and its city code
class Airport(models.Model):
    code= models.CharField(max_length=3)
    city= models.CharField(max_length=64)
    #then I create the string representation of the Airport object
    def __str__(self):
        return f"{self.city} : ({self.code})"
    
#I will also change the appearance of the Flight class from how it looked above to what you see below
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()
