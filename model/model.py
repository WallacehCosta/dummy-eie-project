from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InferInput(BaseModel):
    inputs: list

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/infer")
def infer(data: InferInput):
    return {"outputs": data.inputs}
