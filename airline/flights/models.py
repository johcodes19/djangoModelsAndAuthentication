from django.db import models

# Create your models here.
class Flight(models.Model):
    #this class called flight will have all the properties a flight should have
    origin= models.CharField(max_length=64)
    destination= models.CharField(max_length=64)
    duration= models.IntegerField()
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
    '''
    def __str__(self) :
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes"