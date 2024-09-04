from datetime import datetime
from typing import Any, Dict, List
from pydantic import ValidationError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from core.security import get_hashed_password
from sqlalchemy.orm import Session
from appv1.schemas.miguel_schemas.check_in import CheckInCreate, CheckInEdit, CheckInResponse, EquipajeEnum, LlegadaEnum, MedioLlegadaEnum, HuespedDetail, ReservaDetail




#crear factura
def create_checkin_sql(db: Session, check_in:CheckInCreate ):
    try:
        sql_query = text(
            "INSERT INTO check_in (id_reserva, medio_llegada, llegada_situacion, equipaje) "
            "VALUES (:id_reserva, :medio_llegada, :llegada_situacion, :equipaje)"
        )
        params = {
            "id_reserva": check_in.id_reserva,
            "medio_llegada": check_in.medio_llegada,
            "llegada_situacion": check_in.llegada_situacion,
            "equipaje": check_in.equipaje,
        }
        db.execute(sql_query, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de la check in ya existe.")
            if 'for key \'id_check_in\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. ha ocurrido un error al crear check in")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear check in")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear factura: {e}")
        raise HTTPException(status_code=500, detail="Error al crear check in")
    
    
    
def get_check_in_by_id(db: Session, id_check_in: int) -> CheckInResponse:
    try:
        sql = text(
            """
            SELECT 
                check_in.id_check_in,
                check_in.id_reserva,
                check_in.medio_llegada,
                check_in.llegada_situacion,
                check_in.equipaje,
                reservas.fecha_reserva,
                reservas.empresa,
                reservas.valor_deposito,
                reservas.forma_pago,
                huespedes.nombre_completo,
                huespedes.numero_documento
            FROM check_in
            JOIN reservas ON check_in.id_reserva = reservas.id_reserva
            JOIN huespedes ON reservas.id_huesped = huespedes.id_huesped
            WHERE check_in.id_check_in = :id_check_in
            """
        )
        
        result = db.execute(sql, {"id_check_in": id_check_in}).fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Check-in not found")

        # Convertir los resultados a un diccionario
        result_dict = dict(result._mapping)

        # Asegúrate de que 'fecha_reserva' sea un tipo date
        if isinstance(result_dict["fecha_reserva"], datetime):
            result_dict["fecha_reserva"] = result_dict["fecha_reserva"].date()

        # Crear instancias de los modelos Pydantic
        try:
            check_in = CheckInResponse(
                id_check_in=result_dict["id_check_in"],
                reserva=ReservaDetail(
                    id_reserva=result_dict["id_reserva"],
                    fecha_reserva=result_dict["fecha_reserva"],  # Aquí debería ser tipo 'date'
                    empresa=result_dict["empresa"],
                    valor_deposito=result_dict["valor_deposito"],
                    forma_pago=result_dict["forma_pago"]
                ),
                huesped=HuespedDetail(
                    nombre_completo=result_dict["nombre_completo"],
                    numero_documento=result_dict["numero_documento"]
                ),
                medio_llegada=MedioLlegadaEnum(result_dict["medio_llegada"]),
                llegada_situacion=LlegadaEnum(result_dict["llegada_situacion"]),
                equipaje=EquipajeEnum(result_dict["equipaje"])
            )
        except ValidationError as e:
            print(f"Validation error: {e.json()}")
            raise HTTPException(status_code=422, detail=f"Validation error: {e}")

        return check_in

    except SQLAlchemyError as e:
        print(f"Error al buscar check_in: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar check_in")
    
    




def get_all_check_in(db: Session) -> List[CheckInResponse]:
    try:
        sql = text("""
            SELECT 
                check_in.id_check_in,
                reservas.id_reserva,
                huespedes.nombre_completo,
                huespedes.numero_documento,
                reservas.fecha_reserva,
                reservas.empresa,
                reservas.valor_deposito,
                reservas.forma_pago,
                check_in.medio_llegada,
                check_in.llegada_situacion,
                check_in.equipaje
            FROM check_in
            INNER JOIN reservas ON reservas.id_reserva = check_in.id_reserva
            INNER JOIN huespedes ON reservas.id_huesped = huespedes.id_huesped;
        """)

        result = db.execute(sql).fetchall()

        check_in_list = []
        for row in result:
            # Convertir la fila a un diccionario
            row_dict = dict(row._mapping)  # _mapping convierte la fila en un diccionario

            # Convertir 'fecha_reserva' de datetime a date si es necesario
            if isinstance(row_dict["fecha_reserva"], datetime):
                row_dict["fecha_reserva"] = row_dict["fecha_reserva"].date()

            try:
                check_in = CheckInResponse(
                    id_check_in=row_dict["id_check_in"],
                    reserva=ReservaDetail(
                        id_reserva=row_dict["id_reserva"],
                        fecha_reserva=row_dict["fecha_reserva"],  # Asegúrate de que este campo es tipo 'date'
                        empresa=row_dict["empresa"],
                        valor_deposito=row_dict["valor_deposito"],
                        forma_pago=row_dict["forma_pago"]
                    ),
                    huesped=HuespedDetail(
                        nombre_completo=row_dict["nombre_completo"],
                        numero_documento=row_dict["numero_documento"]
                    ),
                    medio_llegada=MedioLlegadaEnum(row_dict["medio_llegada"]),
                    llegada_situacion=LlegadaEnum(row_dict["llegada_situacion"]),
                    equipaje=EquipajeEnum(row_dict["equipaje"])
                )
                check_in_list.append(check_in)
            except ValidationError as e:
                print(f"Error de validación en la fila: {row_dict}, Error: {e}")
                raise HTTPException(status_code=422, detail=f"Validation error: {e}")

        return check_in_list

    except SQLAlchemyError as e:
        print(f"Error al buscar check_in: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar check_in")
    
    
    
def update_check_in(db: Session, id_check_in: int, check_in_update: CheckInEdit):
    try:
        # Crear un diccionario con los campos a actualizar
        update_fields = {}
        if check_in_update.id_reserva is not None:
            update_fields['id_reserva'] = check_in_update.id_reserva
        if check_in_update.medio_llegada is not None:
            update_fields['medio_llegada'] = check_in_update.medio_llegada
        if check_in_update.llegada_situacion is not None:
            update_fields['llegada_situacion'] = check_in_update.llegada_situacion
        if check_in_update.equipaje is not None:
            update_fields['equipaje'] = check_in_update.equipaje

        if not update_fields:
            raise HTTPException(status_code=400, detail="No fields to update")

        # Construir la consulta de actualización
        sql_query = text("UPDATE check_in SET "
                         + ", ".join([f"{key} = :{key}" for key in update_fields.keys()]) +
                         " WHERE id_check_in = :id_check_in")

        # Agregar el ID del check_in a los parámetros
        params = {**update_fields, "id_check_in": id_check_in}

        # Ejecutar la consulta
        db.execute(sql_query, params)
        db.commit()

        return {"detail": "Check-in updated successfully"}

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de check-in ya existe.")
            if 'for key' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. Ha ocurrido un error al actualizar check-in.")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar check-in.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar check_in: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar check_in")
    
    
def delete_check_in(db: Session, id_check_in: int):
    try:
        # Consulta para eliminar el registro
        sql_query = text("DELETE FROM check_in WHERE id_check_in = :id_check_in")
        
        # Ejecutar la consulta
        result = db.execute(sql_query, {"id_check_in": id_check_in})
        db.commit()

        # Verificar si se eliminó algún registro
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Check-in not found")

        return {"detail": "Check-in deleted successfully"}

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al eliminar check_in: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar check_in")