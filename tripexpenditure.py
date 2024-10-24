def hotel_cost(night):
    return 140 * night

def plane_ride_cost(city):
    if "Charlotte" == city :
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city :
        return 222
    elif "Los Angeles" == city :
        return 475
    
def rental_car_cost(days):
    if days >= 7 :
        return 40 * days - 50
    elif days >= 3 :
        return 40 * days - 20
    else :
        return 40 * days

def trip_cost( city ,  days  , spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of Car rental is " , rental_car_cost(6))
print("Cost of plane ride is  " , plane_ride_cost("Los Angeles"))
print("Cost of hotel room is " , hotel_cost(7))
print("total cost of the trip is " , trip_cost("Tampa", 7 , 500))

    