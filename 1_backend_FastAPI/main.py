from fastapi import FastAPI
from appv1.routers.nicolas_route import impuesto
from appv1.routers.nicolas_route import producto
from appv1.routers.juanca_routers import habitacion


app = FastAPI()

app.include_router(impuesto.router, prefix="/impuesto", tags=["impuesto"])
app.include_router(producto.router, prefix="/producto", tags=["producto"])
app.include_router(habitacion.router, prefix="/habitacion", tags=["habitacion"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
