import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature... ")
        time.sleep(3)


t=threading.Thread(target=monitor_tea_temp,daemon=True)
t.start()

time.sleep(5)  # Just to ensure the monitoring thread has started before the main program ends
print("Main Program Done")

# Explanation:
'''
In this code, we create a thread that runs the `monitor_tea_temp` function, which continuously monitors the tea temperature every 3 seconds.
By setting `daemon=True`, we make this thread a daemon thread, which means it will 
automatically exit when the main program finishes. 
The main program sleeps for 5 seconds before printing "Main Program Done", 
so the monitoring thread runs once (at 3 seconds) before the main thread completes at 5 seconds.
Since the daemon thread automatically exits when the main program finishes, the monitoring thread stops and we won't see any further output after that point.
'''

# OUTPUT
'''
Monitoring tea temperature... 
Main Program Done
'''