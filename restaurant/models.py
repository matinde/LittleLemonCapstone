from django.db import models
from datetime import datetime
 
class Booking(models.Model):
    name = models.CharField(max_length=200)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self): 
        return self.name

class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.IntegerField() 

   def __str__(self):
        return f'{self.title} : {str(self.price)}' 