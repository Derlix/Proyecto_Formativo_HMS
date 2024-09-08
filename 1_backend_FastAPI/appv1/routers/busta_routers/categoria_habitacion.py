from typing import List
from appv1.crud.busta_crud.categoria_habitacion import get_all_room_categories,get_room_categorie_name,create_room_categorie_name
from appv1.schemas.busta_schemas.categoria_habitacion import CategoriaHabitacionResponse,CategoriaHabitacionCreate
from fastapi import APIRouter,Depends,HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore

router = APIRouter()

@router.post("/create")
async def insert_category(category: CategoriaHabitacionCreate, db: Session = Depends(get_db)):
    respuesta = create_room_categorie_name(db, category)
    if respuesta:
        return {"mensaje":"Categoria registrado con exito"}
    else:
        return {"mensaje":"La categoria no se ha podido registrar con exito"}

@router.post("/get-all_room_categories/",response_model = List[CategoriaHabitacionResponse])
async def real_all_room_categories(db: Session = Depends(get_db)):
    room_categories = get_all_room_categories(db)
    if len(room_categories) == 0:
        raise HTTPException(status_code=404, detail="No hay categorias")
    return room_categories

@router.post("/get_room_categorie_name/",response_model = CategoriaHabitacionResponse)
async def read_category_by_name(p_category_name: str, db: Session = Depends(get_db)):
    room_categorie_name = get_room_categorie_name(db, p_category_name)
    if room_categorie_name is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return room_categorie_name
