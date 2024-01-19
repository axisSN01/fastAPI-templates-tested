import uvicorn
from fastapi import FastAPI
from app.routes.routes import routes
from pathlib import Path
import logging

# Configure the root logger to output logs to the console
logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(routes, prefix="/instagram")

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", 
                host="0.0.0.0", 
                port=8000,
                log_level="debug", 
                reload=True
                )
