from fastapi import FastAPI

## This is the ROUTER
app = FastAPI()

## This is the endpoint
@app.get("/")
def hello():
    return {"message":"Hello World"}

@app.get("/about")
def about():
    return {"message":"This is Reddappa Reddy.i want start my career in data field"}