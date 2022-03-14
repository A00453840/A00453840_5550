# A00453840_5550

This repository is for the MCDA 5550 - REST API Project

Database configurations can be changed in BookMyRoom/settings.py


GET API: http://127.0.0.1:8000/app/hotels/

Response:

[
    {
        "hotel_name": "Hotel1",
        "price": 450,
        "availability": true
    },
    {
        "hotel_name": "Hotel2",
        "price": 400,
        "availability": false
    },
    {
        "hotel_name": "Hotel3",
        "price": 500,
        "availability": true
    }
]


POST API: http://127.0.0.1:8000/app/reserve/

Body:

{
   "hotel_name" : "Hotel1", 
   "checkin" : "2022-04-04", 
   "checkout": "2022-04-06", 
    "guests_list": [  
           { 
             "guest_name" : "Nikhil", 
             "gender": "Male" 
           }
       ] 
}

Response:

{
    "confirmation_number": "8371792458"
}
