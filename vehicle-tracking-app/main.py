from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.user import router as user_router
from app.routes.vehicle import router as vehicle_router
app = FastAPI()

     
@app.get('/')
def health_check():
    return JSONResponse(content= {"status":"Running"})

app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(vehicle_router, prefix="/api/v1", tags=["vehicles"])