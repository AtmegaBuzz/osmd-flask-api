from flask import request, jsonify
from models import (
    db,
    Booking,
    CabGroup,
)

import random
from utils.algoritm import main
from utils.decorators import check_auth

@check_auth
def BookCab(user):
    destination = request.json.get("destination")
    time = request.json.get("time")
    date = request.json.get("date")

    try:
            # booking having status code ongoing
            bookings_ongoing = Booking.query.filter_by(status=0).all()

            booking = Booking(destination=destination,user=user)
            db.session.add(booking)
            db.session.commit()


            # create bookings if there are more than 4 ongoing request in queue
            if bookings_ongoing.__len__()>=4:

                groups =  main()

                for group in groups:
                    name = f"grp{random.randint(1,10000)}:{random.randbytes(10000)}"
                    
                    # create a new group(group=cab)
                    grp = CabGroup(name=name)
                    db.session.add(booking)
                    db.session.commit()
                    
                    
                    for usrAttr in group:
                    
                        booking_a = Booking.query.filter_by(id=usrAttr.booking_id)
                        booking_a.status = 1
                        booking_a.group = grp.id
                        booking_a.cost = usrAttr.cost,
                        booking_a.distance = usrAttr.distance
                        
                        db.session.add(booking_a)
                        db.session.commit()
                        
                           
                    
            else:
                return jsonify({"message":"request added successfuly"})
            
                
    except Exception:
        return jsonify({"messge":"allocation failed try again later!"})


@check_auth
def ListBookings(user):
    
    if request.method=="GET":
        bookings = Booking.query.filter_by(user_id=user.id)

        booking_values = []

        for booking in bookings:
            data = {
                "destination":booking.destination,
                "status":booking.status,
                "cost":booking.cost,
                "distance":booking.distance,
                "group":booking.group_id
            }
            booking_values.append(data)

        return jsonify(booking_values),200

    return jsonify({"method":"not allowed"})

