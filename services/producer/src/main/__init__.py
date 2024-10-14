import uvicorn

from fastapi import FastAPI

producer_app = FastAPI()

from src.api import *

if __name__ == "__main__":
    uvicorn.run(producer_app, host="0.0.0.0", port=30001)
