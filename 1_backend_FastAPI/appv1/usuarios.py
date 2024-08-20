from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from appv1.schemas.usuarios import UsuarioCreate
from core.security import get_hashed_password
from core.utlis import generateuser_id
from sqlalchemy import text
from sqlalchemy.orm import Session

#Crear un usuario

def create_usuario_sql(db: Session, usuario: UsuarioCreate):
    try:
        sql_query = text(
            "INSERT INTO usuarios (id_usuario, nombre_completo, email, passhash, usuario_rol, id_hotel) "
            "VALUES (:usuario_id, :nombre_completo, :email, :passhash, :usuario_rol, :id_hotel)"
        )

        params = {
            "usuario_id": generateuser_id(),
            "nombre_completo": usuario.nombre_completo,
            "email": usuario.email,
            "passhash": get_hashed_password(usuario.passhash),
            "usuario_rol": usuario.usuario_rol,
            "id_hotel": usuario.id_hotel,
        }

        db.execute(sql_query, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El id generado automáticamente ya existe, vuelva a intentarlo.")
            if 'for key \'email\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado.")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay integridad de datos al crear el usuario")
