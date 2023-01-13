from datetime import datetime, timedelta
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
# from routers import token, users, rozliv
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# app.include_router(token.router)
# app.include_router(users.router)
# app.include_router(rozliv.router)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)