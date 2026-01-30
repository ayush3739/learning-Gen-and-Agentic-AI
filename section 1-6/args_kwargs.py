# def make_chai():
#     return 'here is tyour masala chai'

# return_value=make_chai()

# print(return_value)

def ideal_chaiwala():
    pass

print(ideal_chaiwala())

def sold_cups():
    return 102

total=sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left==0:
        return 'sorry chai Over'
    return 'chai is ready'
    print('chai')

print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100,200,10 # sold, remaining

sold,_,remaining=chai_report()
print('SoldL',sold)
print('remaining',remaining)