from http.client import HTTPException
from appv1.schemas.nicolas_schemas.Productos import ProductoBase, ImpuestoUpdate, ProductoUpdate
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from sqlalchemy.exc import SQLAlchemyError,IntegrityError # type: ignore
from fastapi import  HTTPException # type: ignore

def create_products(db: Session, product:ProductoBase):
    try:
        sql_query = text(
        "INSERT INTO productos(nombre_producto, descripcion, precio_actual)"
        "VALUES (:nombre_producto, :descripcion, precio_actual)"
        
        )
        params = {
            "nombre_producto": product.nombre_producto,
            "descripcion": product.descripcion,
           "precio_actual": product.precio_actual
        }
        db.execute(sql_query, params)
        db.commit()
        return True 
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear producto: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El id del producto ya existe")
            else:
                raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear producto")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear producto: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el producto")

def get_all_products(db: Session):
    try:
        sql = text("SELECT * FROM productos")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar productos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar productos")
    
def update_product(db: Session, id_producto: str, producto: ProductoUpdate):
    try:
        sql = "UPDATE productos SET "
        params = {"id_producto": id_producto}
        updates = []
        if producto.nombre_producto:
            updates.append("nombre_producto = :nombre_producto")
            params["nombre_producto"] = producto.nombre_producto
        if producto.descripcion:
            updates.append("descripcion = :descripcion")
            params["descripcion"] = producto.descripcion
        if producto.precio_actual:
            updates.append("precio_actual = :precio_actual")
            params["precio_actual"] = producto.precio_actual

        sql = text(sql)

        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al actualizar producto: {e}")
        if not id_producto:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar producto")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar producto: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar producto")
   

def delete_tax(db: Session, id_producto: int):
    try:
        sql = text("DELETE FROM productos WHERE id_producto = :id_producto")
        db.execute(sql, {"id_producto": id_producto})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar producto: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar producto")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar producto: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar producto")