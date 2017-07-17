from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from journey_management.models import Person, Journey, Booking, Payment


class PersonSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Person
        fields = ('id', 'fName', 'lName', 'telephone', 'email', 'type')


class JourneySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Journey
        fields = ('id', 'departure_from', 'departure_to', 'depart_time', 'depart_date', 'driver', 'available_space', 'amount')


class BookingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Booking
        fields = ('id', 'journey', 'client', ' booking_date', 'booking_time')
        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=('client', 'booking_date', 'booking_time')
            )
        ]


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Payment
        fields = ('id', 'client', 'journey', ' payment_date', 'payment_time')



