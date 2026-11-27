from fastapi import FastAPI
from controller import estudiantes_controller

app=FastAPI()

app.include_router(estudiantes_controller.router)
