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
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status() 
            return response.json()
    except httpx.HTTPStatusError as e:
        print("f Error on response {e.response.status_code} - {e.response.text}")
        return {"error": "f HTTP error {e.response.status_code}" }
    except httpx.RequestError as e:
        print(f" Error on request {str(e)}")
        return {"error" : "request error"}

