import httpx
import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()

async def main():
    data = await get_data()
    for key, value in data.items():
        print(f'{key}:{value}')

asyncio.run(main())