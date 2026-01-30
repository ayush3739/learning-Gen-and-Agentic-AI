def pure_func(cups):
    return cups*10

total_cups=0

#not Recommended
def impure_func(cups):
    global total_cups
    total_cups+=cups


#lambda Functions
car_types=['light','kadak','ginger','kadak']

strong_car=list(filter(lambda chai: chai=='kadak',car_types))
print(strong_car)