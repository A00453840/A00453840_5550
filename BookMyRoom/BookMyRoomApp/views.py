from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers
from .models import Hotels


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
        print("In POST")
        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"Message": "Added Successfully"})


@api_view(['GET', 'POST'])
def Hotels_detail(request,pk):
    if request.method == 'GET':
        hotels_list = Hotels.objects.get(id=pk)
        hotelSerializer = HotelSerializers(hotels_list, many=False)
        return Response(hotelSerializer.data)


