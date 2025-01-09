from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import auth, userController
from app.db.database import init_db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(auth.router, prefix="", tags=["auth"])
app.include_router(userController.router, prefix="/user", tags=["update user"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)