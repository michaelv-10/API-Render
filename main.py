from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your API is working"}

@app.get("/hello")
def hello():
    return{"message": "Hello from your free API"}