from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.producto import get_product_by_id, get_products, get_product, add_product, delete_product
from config.database import get_db

router = APIRouter()

@router.get("/products")
def get_products_route(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/products/{product_id}")
def get_product_route(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(product_id, db)

@router.post("/products")
def add_product_route(product: dict, db: Session = Depends(get_db)):
    return add_product(product, db)

@router.delete("/products/{product_id}")
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    return delete_product(product_id, db)
