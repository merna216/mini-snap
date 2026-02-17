from fastapi import FastAPI
app = FastAPI()
@app.get("/")

async def root():
    return {"message": "Mini Snap API is running 🚀"}