from fastapi import FastAPI
from appv1.routers.nicolas_route import impuesto

app = FastAPI()

app.include_router(impuesto.router, prefix="/impuesto", tags=["impuesto"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
