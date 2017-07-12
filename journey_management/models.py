import uuid

from django.db import models


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Client(models.Model):
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
    driver = models.ForeignKey(Client, on_delete=models.CASCADE)
    available_space = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.client, self.journey)


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s %s" % (self.client, self.journey)


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True, editable=False)
    payment_time = models.TimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s %s" % (self.client, self.journey)



