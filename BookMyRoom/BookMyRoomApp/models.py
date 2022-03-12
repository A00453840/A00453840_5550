from django.db import models

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    availability = models.BooleanField(null=False,default=False)

    def __str__(self):
        return self.name

class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)