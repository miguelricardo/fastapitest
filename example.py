import httpx
import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/")
        print(response.json)
        return response.json()

async def main():
    data = await get_data()
    for key, value in data.items():
        print(f'{key}:{value}')

asyncio.run(main())