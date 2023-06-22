from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{nama}")
async def name(nama):
    return {"message":f"Halo, nama saya adalah {nama}"}