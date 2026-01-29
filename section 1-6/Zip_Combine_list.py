'''You're preparing an order summary with customer names
and their total bill.
Task:
· Use two lists: one for names and one for bills.
· Print: "[Name] paid ₹[amount]
'''

names=['ayush','meera','sam','yash','kishan','aman']
bills=[40,50,20,80,90]

for item in zip(names,bills):
    print(item)

for names,bills in zip(names,bills):
    print(f'{names} paid {bills} rupees')