from typing import Annotated
from appv1.crud.usuarios import get_usuarios_by_email,get_usuarios_by_email
from fastapi import APIRouter,Depends, HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from core.security import get_hashed_password,verify_password,create_access_token,verify_token
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/access/token")

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    user = await verify_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_db =get_usuarios_by_email(db, user)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not user_db.user_status:
        raise HTTPException(status_code=403, detail="User Deleted, Not authorized")
    return user_db


def authenticate_user(username: str, password: str,db: Session):
    user = get_usuarios_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.passhash):
        return False
    return user


# @router.get("/login/",response_model = dict)
# async def access(email:str, password: str, db: Session = Depends(get_db)):
#     usuario = get_usuarios_by_email(db, email)
#     if usuario is None:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#     # verificacion de password
#     resultado = verify_password(password, usuario.passhash)
#     if not resultado:
#         raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
#     data = {"sub":usuario.user_id,"rol":usuario.user_role}
#     token = create_access_token(data)

#     return {"token":token}


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user( form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Datos incorrectos en email o password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.user_id, "rol":user.user_role}
    )
    return {"access_token":access_token, "token_type":"bearer"}