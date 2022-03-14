from django.db import models
from .utils import create_new_ref_number


class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    availability = models.BooleanField(null=False,default=False)

    def __str__(self):
        return self.name

#
# class HotelsList(models.Model):
#     id = models.AutoField(primary_key=True)
#     hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


class Reserve(models.Model):
    hotel_name = models.CharField(max_length=200, null=False)
    # hotel_name = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    checkin = models.CharField(max_length=200, null=False)
    checkout = models.CharField(max_length=200, null=False)
    # guests_list = models.ForeignKey(Guest, on_delete=models.CASCADE)
    confirmation_number = models.CharField(max_length=10,blank=True,editable=False,unique=True,
                                           default=create_new_ref_number)

    def __str__(self):
        return self.confirmation_number


class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
