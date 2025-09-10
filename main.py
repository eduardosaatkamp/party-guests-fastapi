from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá, mundo!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Olá, {name}! Seja bem-vindo ao FastAPI 🚀"}
