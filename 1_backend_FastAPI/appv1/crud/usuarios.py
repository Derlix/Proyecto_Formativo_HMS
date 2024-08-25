from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from appv1.schemas.usuarios import UsuarioCreate,UsuarioUpdate
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
        sql = text("SELECT * FROM usuarios WHERE usuario_estado = true ")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuarios: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuarios")



def get_all_users_by_rol(db: Session, p_rol_name: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE usuario_rol = :p_rol_name ")
        result = db.execute(sql,{"usuario_rol":p_rol_name}).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuarios: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuarios")
    
    

def update_user(db: Session, id_usuario: str, user: UsuarioUpdate):
    try:
        sql = "UPDATE usuarios SET "
        params = {"id_usuario": id_usuario}
        updates = []
        if user.nombre_completo:
            updates.append("nombre_completo = :nombre_completo")
            params["nombre_completo"] = user.nombre_completo
        if user.email:
            updates.append("email = :email")
            params["email"] = user.email
        if user.usuario_rol:
            updates.append("usuario_rol = :usuario_rol")
            params["usuario_rol"] = user.usuario_rol
        if user.usuario_estado is not None:
            updates.append("usuario_estado = :usuario_estado")
            params["usuario_estado"] = user.usuario_estado
        
        for  ind, valor in  enumerate(updates):
            if len(updates) - 1 == ind:
                sql += valor
            else:
                sql += valor + ", "
        print(sql)
        sql += " WHERE id_usuario = :id_usuario"
        # Envuelve la consulta SQL en text()
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al actualizar usuario: {e}")
        if 'for key \'email\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar usuario")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al actualizar usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar usuario")


def get_all_users_paginated(db: Session, page: int = 1, page_size: int = 10):
    try:
        # Calcular el offset basado en el número de página y el tamaño de página
        offset = (page - 1) * page_size

        # Consulta SQL con paginación, incluyendo todos los campos requeridos
        sql = text(
            "SELECT id_usuario, nombre_completo, email, usuario_rol, usuario_estado, creado_en, actualizado_en "
            "FROM usuarios "
            "ORDER BY creado_en DESC "  # Cambia esto por tu criterio de ordenación
            "LIMIT :page_size OFFSET :offset"
        )
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        # Obtener el número total de usuarios
        count_sql = text("SELECT COUNT(*) FROM usuarios")
        total_users = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_users + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al obtener todos los usuarios: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener todos los usuarios")
    

def delete_usuarios(db: Session, id_usuario: str):
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
    