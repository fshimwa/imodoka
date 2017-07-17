import uuid

from django.db import models
from rest_framework.validators import UniqueTogetherValidator


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    departure_from = models.CharField(max_length=255)
    departure_to = models.CharField(max_length=255)
    depart_time = models.CharField(null=True, max_length=255)
    depart_date = models.DateField(null=True)
    driver = models.ForeignKey(Person, on_delete=models.CASCADE)
    available_space = models.CharField(max_length=255)
    amount = models.IntegerField()


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    journey = models.ForeignKey(Journey, related_name='journey', on_delete=models.CASCADE)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True, editable=False)
    payment_time = models.TimeField(auto_now_add=True, editable=False)

