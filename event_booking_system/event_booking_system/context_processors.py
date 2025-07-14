from bookings.models import Event
from django.utils.timezone import now

def next_event(request):
    upcoming = Event.objects.filter(date__gte=now()).order_by('date')
    next_available = next((e for e in upcoming if e.seats_left() > 0), None)
    return {
        'next_event': next_available
    }
