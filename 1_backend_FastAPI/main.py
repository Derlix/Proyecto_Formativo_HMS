from fastapi import FastAPI
from appv1.routers.nicolas_route import impuesto
from appv1.routers.nicolas_route import producto

app = FastAPI()

app.include_router(impuesto.router, prefix="/impuesto", tags=["impuesto"])
app.include_router(producto.router, prefix="/producto", tags=["producto"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
