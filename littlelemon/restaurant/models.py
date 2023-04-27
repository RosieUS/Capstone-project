from django.db import models

# Create your models here.

class Booking(models.Model):
    Id = models.IntegerField(primary_key= True, default= 1)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField
    BookingDate = models.DateTimeField

    def __str__(self): 
        return self.Name

class Menu(models.Model):
    Id = models.IntegerField(primary_key= True, default= 1)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField

    def __str__(self): 
        return self.title
    
class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'