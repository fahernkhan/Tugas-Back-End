#Json object
from fastapi import FastAPI
from pydantic import BaseModel

class Biodata(BaseModel):
    nama: str
    usia: integer
    asal: str

app = FastAPI()

@app.post("/biodata/")
async def create_biodata(biodata: Biodata):
    return biodata