# Django-Developer

# Event & Ticket Booking System (Django)

A web application that allows users to browse and book seats for upcoming community events, while providing admins with full control to manage events and view bookings.

---
## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/NivethaMercy110211/Django-Developer.git
cd event-booking-system
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note**: Make sure Pillow is installed for image support.

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```


## Features Checklist

- Custom user model
- Event image upload (with preview)
- Sold-out detection
- Booking with seat validation
- Booking confirmation page + email (console)
- Progress bar for seat booking
- Pagination
- Admin interface (inline bookings)
- Custom template filter + context processor


### Visitors
- Browse upcoming events
- View event details (description, date, seat availability)
- Book seats via form (name, email, number of seats)
- See seat availability with a live progress bar
- View booking confirmation
- Console email confirmation

### Admin
- Admin login with custom user model
- Add, edit, delete events
- Upload event images
- Auto-track sold-out status
- View all bookings per event (inline in admin)
- See visual image preview in admin list

### Extras
- Seat progress bar (`% booked`) with color styling
- Pagination in event list
- Custom template filters
- Context processor for "Next Upcoming Event"
- Static and media file handling

---

## Project Structure

```
event_booking_system/
├── accounts/              # Custom user model
├── bookings/              # Events, bookings, templates, filters
├── static/                # CSS and static assets
├── media/                 # Uploaded event images
├── templates/             # HTML templates
├── event_booking_system/  # Settings and core config
```

---


