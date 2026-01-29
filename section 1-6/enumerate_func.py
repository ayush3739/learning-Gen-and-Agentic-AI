'''
You're creating a tea menu board.
Each item must be numbered.
Task:
· Use enumerate() 
to print menu items with numbers.
'''

menu=["Green",'lemon','apple','banana','orange']


# for m in menu:
#     print(m)

# Using Enumerate 

a=list(enumerate(menu))
print(a)

b=list(enumerate(menu,start=1))
print(b)

for idx,item in enumerate(menu,start=1):
    print(f'{idx} : {item} chai')


# Unpacking
c,d,e=('green','blue',8)
print(f'{c} - {d}')

# Packing
t = 'green', 'blue', 8   # packed into a tuple
print(t)                 # ('green', 'blue', 8)

def colors():
    return 'green', 'blue', 8  # returns a tuple

p = colors()
print(p)

a, *rest = 1, 2, 3, 4
# a = 1, rest = [2, 3, 4]
print(f'{a} - {rest}')