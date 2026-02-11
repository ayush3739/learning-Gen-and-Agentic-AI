import asyncio
import time

async def brew(name):
    print(f'Brewing {name}...')
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f'{name} is ready!')

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew('ginger tea'),
        brew('lemon tea')
    )


asyncio.run(main())