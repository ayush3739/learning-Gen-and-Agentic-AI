# without walrus operator
# value =13
# remainder=value%5
# if remainder: print(f"Not divisible , remainder is {remainder}")

# with Walrus operator

value=13
if (remainder :=value % 5):
    print(f"Not divisible , remainder is {remainder}")
    # Not divisible , remainder is 3

available_sizes=['small','medium','large']
if (requested_size := input('Enter your chai cup size : ')) in available_sizes:
    print(f'Serving  - {requested_size}')
else:
    print(f'size is unavailable - {requested_size}')
    
flavours=['masala','ginger','mint','plain']
print('Available Flavours',flavours)

while (flavor := input("Chooses your flavor : ")) not in flavours:
    print(f'Sorry ,{flavor} is not available')
print(f'You choose {flavor}')
