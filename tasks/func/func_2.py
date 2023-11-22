# create an update_car_info func in which 
# all named arguments will be combined into 
# a car dictionary

# add a new is_available key to the dictionary 
# with the value True

# return modified dict from the func

# call a func with brand and price keyword args, their values
# can be any

# output the result of the func call to the terminal


def update_car_info(**kwargs):
    car = {}
   
    for key, value in kwargs.items():
        car[key] = value
        car['is_available'] = True
        return car
        
# Test the function
cars = update_car_info(brand='Toyota', price=25000)
print(cars)