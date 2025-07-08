from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.booking_date} at {self.booking_time}"
    
class AdminUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.name
