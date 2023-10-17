from django.db import models

# Create your models here.
class Flight(models.Model):
    #this class called flight will have all the properties a flight should have
    origin= models.CharField(max_length=64)
    destination= models.CharField(max_length=64)
    duration= models.IntegerField()
    #from here I will create migrations to tell django to take into account the changes I have made in my models and put them in a database
    #to do that, you go to the terminal and type python manage.py makemigrations