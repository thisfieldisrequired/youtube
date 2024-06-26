import uvicorn
from fastapi import FastAPI

from api import router as api_router

app = FastAPI()
app.include_router(
    api_router,
    prefix="/api",
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
