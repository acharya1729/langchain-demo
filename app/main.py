# your_project/app/main.py
from fastapi import FastAPI
from app.fastapi_app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
