from rest_framework import serializers
from .models import Hotels, Guest, Reserve


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Hotels
        exclude = ['id']
        # fields = ['hotel_name','price','availability']


# class HotelNameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Hotels
#         fields = ['hotel_name']


# class HotelListSerializers(serializers.ModelSerializer):
#     class Meta:
#         many = True
#         model = HotelsList
#         fields = ['hotels_list']


class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        exclude = ['id']
        # fields = ['guest_name','gender']

class ReservationsSerializers(serializers.ModelSerializer):
    guests_list = GuestSerializers(many=True)
    # hotel_name = HotelNameSerializers(many=False)
    def create(self, validated_data):
        guests_data = validated_data.pop("guests_list")
        reservation = Reserve.objects.create(**validated_data)
        for guest_data in guests_data:
            Guest.objects.create(reserve=reservation, **guest_data)
        return reservation

    class Meta:
        model = Reserve
        fields = ['hotel_name', 'checkin', 'checkout', 'guests_list']
        # depth = 1


class ConfirmationNumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ['confirmation_number']