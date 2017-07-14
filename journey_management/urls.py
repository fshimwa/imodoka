from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DriverView, ClientView, JourneyView, BookingView, PaymentView

urlpatterns = {
    url(r'^Drivers/$', DriverView.as_view(), name="create"),
    url(r'^Clients/$', ClientView.as_view(), name="create"),
    url(r'^Journeys/$', JourneyView.as_view(), name="create"),
    url(r'^Bookings/$', BookingView.as_view(), name="create"),
    url(r'^Payments/$', PaymentView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)