from fastapi import FastAPI

app = FastAPI() #evry fast api app requires a FastAPI Instance

@app.get("/")

def read_root():

    return {"message": "Hello World"}