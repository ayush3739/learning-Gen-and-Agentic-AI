import asyncio
import aiohttp 


async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f'Fetched {url} with status {response.status}')

async def main():
    urls=['http://httpbin.org/delay/2'] * 3
    async with aiohttp.ClientSession() as session:
        tasks= [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks) # '*' means unpacking the list of tasks into individual arguments for gather

asyncio.run(main())