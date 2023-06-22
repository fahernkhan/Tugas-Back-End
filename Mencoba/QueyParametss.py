from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{nama}")
async def name(nama, age, from):
    return {"message":f"Halo nama saya adalah {nama}, berusia {age}, dan berasal dari {from}"}