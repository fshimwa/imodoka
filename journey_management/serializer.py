from rest_framework import serializers

from journey_management.models import Driver, Client, Journey, Booking, Payment


class DriverSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Driver
        fields = ('id', 'fName', 'lName', 'telephone', 'email', 'type')


class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Client
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
        fields = ('id', 'journey', 'client', ' booking_date')


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Payment
        fields = ('id', 'client', 'journey', ' payment_date', 'payment_time')



