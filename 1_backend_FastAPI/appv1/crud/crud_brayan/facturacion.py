from typing import Any, Dict, List
from pydantic import ValidationError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.schemas_brayan.facturacion  import CheckInDetail, EstadoType, FacturacionCreate, FacturacionResponse, FacturacionUpdate, HuespedDetail, MetodoPagoType, ReservaDetail
from fastapi import HTTPException
#from core.utils import generate_user_id
from core.security import get_hashed_password
from sqlalchemy.orm import Session




#crear factura
def create_facturacion_sql(db: Session, facturacion: FacturacionCreate):
    try:
        sql_query = text(
            "INSERT INTO facturacion (id_check_in, subtotal, impuestos, total, total_precio_productos, metodo_pago, estado, fecha_salida) "
            "VALUES (:id_check_in, :subtotal, :impuestos, :total, :total_precio_productos, :metodo_pago, :estado, :fecha_salida)"
        )
        params = {
            "id_check_in": facturacion.id_check_in,
            "subtotal": facturacion.subtotal,
            "impuestos": facturacion.impuestos,
            "total": facturacion.total,
            "total_precio_productos": facturacion.total_precio_productos,
            "metodo_pago": facturacion.metodo_pago,
            "estado": facturacion.estado,
            "fecha_salida": facturacion.fecha_salida,
        }
        db.execute(sql_query, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de factura ya está en uso")
            if 'for key \'id_facturacion\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. ha ocurrido un error al crear la factura")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear factura")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear factura: {e}")
        raise HTTPException(status_code=500, detail="Error al crear factura")





# Consultar una factura por su id
def get_factura_by_id(db: Session, id_facturacion: int) -> Dict[str, Any]:
    try:
        sql = text(
            """
            SELECT 
                facturacion.id_facturacion,
                check_in.id_check_in,
                facturacion.subtotal,
                facturacion.impuestos,
                facturacion.total,
                facturacion.total_precio_productos,
                facturacion.metodo_pago,
                facturacion.estado,
                facturacion.fecha_salida,
                check_in.id_reserva,
                check_in.medio_llegada,
                check_in.llegada_situacion,
                check_in.equipaje,
                reservas.id_reserva,
                reservas.fecha_reserva,
                reservas.empresa,
                reservas.valor_deposito,
                reservas.forma_pago,
                huespedes.nombre_completo,
                huespedes.numero_documento
            FROM facturacion
            JOIN check_in ON facturacion.id_check_in = check_in.id_check_in
            JOIN reservas ON check_in.id_reserva = reservas.id_reserva
            JOIN huespedes ON reservas.id_huesped = huespedes.id_huesped
            WHERE facturacion.id_facturacion = :id_facturacion
            """
        )
        result = db.execute(sql, {"id_facturacion": id_facturacion}).fetchone()

        if result is None:
            return None

        factura = FacturacionResponse(
            id_facturacion=result.id_facturacion,
            id_check_in=result.id_check_in,
            subtotal=result.subtotal,
            impuestos=result.impuestos,
            total=result.total,
            total_precio_productos=result.total_precio_productos,
            metodo_pago=MetodoPagoType(result.metodo_pago),
            estado=EstadoType(result.estado),
            fecha_salida=result.fecha_salida,
            check_in=CheckInDetail(
                id_reserva=result.id_reserva,
                medio_llegada=result.medio_llegada,
                llegada_situacion=result.llegada_situacion,
                equipaje=result.equipaje
            ),
            reserva=ReservaDetail(
                fecha_reserva=result.fecha_reserva,
                empresa=result.empresa,
                valor_deposito=result.valor_deposito,
                forma_pago=result.forma_pago
            ),
            huesped=HuespedDetail(
                nombre_completo=result.nombre_completo,
                numero_documento=result.numero_documento
            )
        )
        return factura

    except SQLAlchemyError as e:
        print(f"Error al consultar la factura : {e}")
        raise HTTPException(status_code=500, detail="Error al consultar la factura")



#obtener todas las facturas
def get_all_facturas(db: Session) -> List[FacturacionResponse]:
    try:
        sql = text("""
            SELECT
                facturacion.id_facturacion,
                check_in.id_check_in,
                facturacion.subtotal,
                facturacion.impuestos,
                facturacion.total,
                facturacion.total_precio_productos,
                facturacion.metodo_pago,
                facturacion.estado,
                facturacion.fecha_salida,
                check_in.id_reserva,
                check_in.medio_llegada,
                check_in.llegada_situacion,
                check_in.equipaje,
                reservas.id_reserva,
                reservas.fecha_reserva,
                reservas.empresa,
                reservas.valor_deposito,
                reservas.forma_pago,
                huespedes.nombre_completo,
                huespedes.numero_documento
            FROM facturacion
            JOIN check_in ON facturacion.id_check_in = check_in.id_check_in
            JOIN reservas ON check_in.id_reserva = reservas.id_reserva
            JOIN huespedes ON reservas.id_huesped = huespedes.id_huesped
        """)
        result = db.execute(sql).fetchall()
        

        facturas = []
        for row in result:
            try:
                factura = FacturacionResponse(
                    id_facturacion=row.id_facturacion,
                    id_check_in=row.id_check_in,
                    subtotal=row.subtotal,
                    impuestos=row.impuestos,
                    total=row.total,
                    total_precio_productos=row.total_precio_productos,
                    metodo_pago=MetodoPagoType(row.metodo_pago),
                    estado=EstadoType(row.estado),
                    fecha_salida=row.fecha_salida,
                    check_in=CheckInDetail(
                        id_reserva=row.id_reserva,
                        medio_llegada=row.medio_llegada,
                        llegada_situacion=row.llegada_situacion,
                        equipaje=row.equipaje
                    ),
                    reserva=ReservaDetail(
                        fecha_reserva=row.fecha_reserva,
                        empresa=row.empresa,
                        valor_deposito=row.valor_deposito,
                        forma_pago=row.forma_pago
                    ),
                    huesped=HuespedDetail(
                        nombre_completo=row.nombre_completo,
                        numero_documento=row.numero_documento
                    )
                )
                facturas.append(factura)
            except ValidationError as e:
                print(f"Error de validación en la fila: {row}, Error: {e}")
                raise

        return facturas

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar facturas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar facturas")




#actualizar factura
def update_factura(db: Session, id_facturacion: int, factura: FacturacionUpdate):
    try:
        # Verificar si al menos un campo necesita ser actualizado
        updates = []
        sql = "UPDATE facturacion SET "
        params = {"id_facturacion": id_facturacion}
        
        if factura.subtotal is not None:
            updates.append("subtotal = :subtotal")
            params["subtotal"] = factura.subtotal
        if factura.impuestos is not None:
            updates.append("impuestos = :impuestos")
            params["impuestos"] = factura.impuestos
        if factura.total is not None:
            updates.append("total = :total")
            params["total"] = factura.total
        if factura.total_precio_productos is not None:
            updates.append("total_precio_productos = :total_precio_productos")
            params["total_precio_productos"] = factura.total_precio_productos
        if factura.metodo_pago is not None:
            updates.append("metodo_pago = :metodo_pago")
            params["metodo_pago"] = factura.metodo_pago.value
        if factura.estado is not None:
            updates.append("estado = :estado")
            params["estado"] = factura.estado.value
        if factura.fecha_salida is not None:
            updates.append("fecha_salida = :fecha_salida")
            params["fecha_salida"] = factura.fecha_salida

        if not updates:
            raise HTTPException(status_code=400, detail="No hay campos para actualizar")
        sql += ", ".join(updates) + " WHERE id_facturacion = :id_facturacion"
        
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        print(f"Error al actualizar factura: {e}")
        if 'for key \'id_facturacion\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El ID ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar factura")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar factura: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar factura")



    

# Eliminar una factura
def delete_factura(db: Session, id_facturacion: int):
    try:
        sql = text("DELETE FROM facturacion WHERE id_facturacion = :id_facturacion")
        db.execute(sql, {"id_facturacion": id_facturacion})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar factura: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar factura")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar factura: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar factura")
    
