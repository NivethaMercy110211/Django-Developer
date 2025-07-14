from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def seats_left(self):
        booked = sum(booking.num_seats for booking in self.booking_set.all())
        return self.capacity - booked

    def is_sold_out(self):
        return self.seats_left() <= 0

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    num_seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.event.title}"



