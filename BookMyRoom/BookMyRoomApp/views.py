from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers, ReservationsSerializers, ConfirmationNumSerializers
from .models import Hotels, Reserve


def home(request):
    return HttpResponse("<h1> HELLO WORLD </h1>")


@api_view(['GET', 'POST'])
def getListOfHotels(request):
    if request.method == 'GET':
        hotels_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)
    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        # print(hotel_request)
        if serialize_request_data.is_valid():
            # print("Is Valid")
            recordId = serialize_request_data.save()
            print(recordId.id)
            # listSerialize_request_data = HotelListSerializers(data=recordId)
            # if listSerialize_request_data.is_valid():
            #     print("Is Valid")
            #     listSerialize_request_data.save()

        return Response({"Message": "Added Successfully"})


@api_view(['POST'])
def reservationConfirmation(request):
    # if request.method == 'GET':
    #     reservations_list = Reserve.objects.all()
    #     resSerializer = ReservationsSerializers(reservations_list, many=True)
    #     return Response(resSerializer.data)
    if request.method == 'POST':
        reserve_request = request.data
        reserve_request_data = ReservationsSerializers(data=reserve_request)
        # print(reserve_request_data)
        if reserve_request_data.is_valid():
            # print("Is Valid")
            recordId = reserve_request_data.save()
            # print(recordId)
        return Response({"confirmation_number": recordId.confirmation_number})


@api_view(['GET', 'POST'])
def Hotels_detail(request,pk):
    if request.method == 'GET':
        hotels_list = Hotels.objects.get(id=pk)
        hotelSerializer = HotelSerializers(hotels_list, many=False)
        return Response(hotelSerializer.data)


