from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{nama}")
async def name(nama : str, age : int = 20, from : str = 'Bandung'):
    return {"message":f"Halo nama saya adalah {nama}, berusia {age}, dan berasal dari {from}"}