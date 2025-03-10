# import FastAPI framework
from fastapi import FastAPI

#Instace of FastAPI
app = FastAPI()

#Define a route that GET requests at the root URL /
@app.get("/") 
async def root():
    # Return a json response
    return { "message" : "Holamundo!"}