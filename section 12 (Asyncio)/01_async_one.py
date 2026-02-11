import asyncio

# A simple asynchronous function to simulate brewing chai tea.
# It waits for 2 seconds to mimic the brewing time before printing that the chai is ready.
# This demonstrates the use of asyncio for asynchronous programming in Python.
# This script uses asyncio to run the brew_chai function asynchronously.
# Diffrence:- from synchronous code, which would block the execution until the task is complete,
# here we use 'await' to pause the function without blocking the entire program.

async def brew_chai():
    print('Brewing chai...')
    await asyncio.sleep(2)
    print("Chai is ready!")

asyncio.run(brew_chai())
