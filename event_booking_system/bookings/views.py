from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Booking
from .forms import BookingForm
from django.core.mail import send_mail
from django.utils.timezone import now
from django.core.paginator import Paginator



import logging
logger = logging.getLogger(__name__)
logger.info("New booking created")

def event_list(request):
    events = Event.objects.filter(date__gte=now()).order_by('date')
    paginator = Paginator(events, 3)
    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'bookings/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = BookingForm()

    booked = event.capacity - event.seats_left()
    if event.capacity > 0:
        percent_booked = (booked / event.capacity) * 100
    else:
        percent_booked = 0

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            if booking.num_seats <= event.seats_left():
                booking.save()
                send_mail(
                    subject='Booking Confirmation',
                    message=f"Thanks {booking.name}, you've booked {booking.num_seats} seat(s) for '{event.title}'.",
                    from_email='no-reply@example.com',
                    recipient_list=[booking.email],
                    fail_silently=False,
                )
                return redirect('booking_confirmation', pk=booking.pk)
            else:
                form.add_error('num_seats', 'Not enough seats available.')

    booked = event.capacity - event.seats_left()
    percent_booked = int((booked / event.capacity) * 100) if event.capacity else 0

    return render(request, 'bookings/event_detail.html', {
        'event': event,
        'form': form,
        'percent_booked': percent_booked,
        'seats_left': event.seats_left(),
    })


def booking_confirmation(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})
