from sqlalchemy.orm import Session
from models.Producto import Producto
from fastapi import HTTPException

from sqlalchemy.exc import SQLAlchemyError

def get_products(db: Session):
    try:
        # Consultar los productos desde la base de datos
        productos = db.query(Producto).all()

        # Convertir los productos a diccionarios y ordenar las claves
        productos_dict = []
        for producto in productos:
            producto_dict = {
                "id": producto.id,
                "descripcion": producto.descripcion,  # Ajusta esto a "descripcion" si es necesario
                "precio": producto.precio
            }
            productos_dict.append(producto_dict)

        return productos_dict

    except SQLAlchemyError as e:
        # Captura de errores específicos de SQLAlchemy (por ejemplo, error en la base de datos)
        db.rollback()  # Asegúrate de hacer rollback si la transacción falla
        print(f"Error de base de datos: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al consultar productos de la base de datos")

    except Exception as e:
        # Captura de cualquier otro tipo de error
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error inesperado al obtener los productos")


def get_product_by_id(product_id: int, db: Session):
    producto = db.query(Producto).filter(Producto.id == product_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

def add_product(product: dict, db: Session):
    nuevo_producto = Producto(nombre=product["descripcion"], precio=product["precio"])
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return {"message": "Producto agregado", "product": nuevo_producto}

def delete_product(product_id: int, db: Session):
    producto = db.query(Producto).filter(Producto.id == product_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"message": "Producto eliminado"}
