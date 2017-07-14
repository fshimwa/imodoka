from rest_framework import generics

from journey_management.serializer import DriverSerializer, ClientSerializer, JourneySerializer, BookingSerializer, \
    PaymentSerializer
from .models import Driver, Client, Journey, Booking, Payment


class DriverView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Driver."""
        serializer.save()


class ClientView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Client."""
        serializer.save()


class JourneyView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Journey."""
        serializer.save()


class BookingView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Booking."""
        serializer.save()


class PaymentView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Payment."""
        serializer.save()
