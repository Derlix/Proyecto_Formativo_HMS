from typing import List
from appv1.crud.busta_crud.categoria_habitacion import get_all_room_categories,get_room_categorie_name,create_room_categorie_name,get_room_categorie_id,update_categoria_habitacion,get_all_cateogories_paginated
from appv1.schemas.busta_schemas.categoria_habitacion import CategoriaHabitacionResponse,CategoriaHabitacionCreate,CategoriaHabitacionUpdate,PaginatedCategoriaHabitacionResponse
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


# Endpoint para actualizar una categoría de habitación
@router.put("/update_categoria_habitacion/", response_model=dict)
def update_categoria_habitacion_by_id(
    id_categoria_habitacion: int,
    categoria_habitacion: CategoriaHabitacionUpdate,
    db: Session = Depends(get_db),
):
    # Verificar si la categoría de habitación existe
    verify_categoria_habitacion = get_room_categorie_id(db, id_categoria_habitacion)
    if verify_categoria_habitacion is None:
        raise HTTPException(status_code=404, detail="Categoría de habitación no encontrada")
    
    # Actualizar la categoría de habitación solo con los campos proporcionados
    db_categoria_habitacion = update_categoria_habitacion(db, id_categoria_habitacion, categoria_habitacion)
    
    if db_categoria_habitacion:
        return {"mensaje": "Categoría de habitación actualizada con éxito"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo actualizar la categoría de habitación")

# usuarios paginados
@router.get("/categorie-by-page/", response_model=PaginatedCategoriaHabitacionResponse)
def get_all_room_categories_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),):
    categories, total_pages = get_all_cateogories_paginated(db, page, page_size)

    return {
        "categories": categories,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }
