from typing import Annotated
from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from appv1.crud.usuarios import get_usuario_by_id,get_usuarios_by_email
from appv1.schemas.usuarios import UsuarioResponse
from core.security import verify_password,create_access_token,verify_token
from db.database import get_db
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
        user_db = get_usuario_by_id(db, user)
        if user_db is None:
            raise HTTPException(status_code=404, detail="User not found")
        if not user_db.usuario_estado:
            raise HTTPException(status_code=403, detail="User Deleted, Not authorized")
        return user_db

def authenticate_user(username: str, password: str,db:Session):
    user = get_usuarios_by_email(db,username)
    if not user:
        return False
    if not verify_password(password, user.passhash):
        return False
    return user


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db:Session = Depends(get_db)):

    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Datos incoorectos en email o password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.id_usuario,"rol":user.usuario_rol}
    )
    return {"access_token":access_token, "token_type":"bearer"}