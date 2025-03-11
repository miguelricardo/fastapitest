# import FastAPI framework
from fastapi import FastAPI
import httpx

#Instace of FastAPI
app = FastAPI()

#Define a route that GET requests at the root URL /
@app.get("/") 
async def root():
    # Return a json response
    return { "message" : "Holamundo!"}

#Define a route that GET requests at the root URL /
@app.get("/data") 
async def det_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()

