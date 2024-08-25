from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from appv1.schemas.usuarios import UsuarioCreate
from core.security import get_hashed_password
from core.utlis import generateuser_id
from sqlalchemy import text
from sqlalchemy.orm import Session

# crudusuario.py

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
            "id_hotel": usuario.id_hotel,  # Ahora se pasa directamente
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

# Consultar un usuario por su ID
def get_usuario_by_id(db: Session, id_usuario: str):
    sql = text("SELECT * FROM usuarios WHERE id_usuario = :id_usuario")
    result = db.execute(sql, {"id_usuario": id_usuario}).fetchone()
    return result

    # Consultar un usuario por su email
def get_usuarios_by_email(db: Session, email: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE email = :email")
        result = db.execute(sql, {"email": email}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar email por correo: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar email por correo")
    
#consultar todos los usuarios activos
def get_all_users(db: Session):
    try:
        sql = text("SELECT * FROM usuarios WHERE usuario-estad = true ")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuarios: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuarios")


# Eliminar un usuario
def delete_user(db: Session, id_usuario: str):
    try:
        sql = text("UPDATE usuarios SET usuario_estado = 0  WHERE id_usuario = :id_usuario")
        db.execute(sql, {"id_usuario": id_usuario})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar usuario: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar usuario")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar usuario")