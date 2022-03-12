from . import views

from django.urls import path

urlpatterns = [
    path('home/', views.home, name="home"),
    path("hotels/", views.getListOfHotels, name="getListOfHotels"),
    path("hotel_list/<str:pk>", views.Hotels_detail, name="hotelDetail")
]