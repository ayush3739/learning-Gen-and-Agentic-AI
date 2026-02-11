import threading

chai_stock=0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock+=1

threads=[threading.Thread(target=restock) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f'Chai Stock : {chai_stock}') 