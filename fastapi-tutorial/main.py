from fastapi import FastAPI

app = FastAPI()


@app.get("/", description= "This is a minor test", deprecated =True)
async def base_route():
    return {"message": "fastapi demo"}


@app.post("/")
async def post():
    return {"message": "This is a new post in the file"}

@app.put("/")
async def put():
    return {"message":"This is my out test"}
