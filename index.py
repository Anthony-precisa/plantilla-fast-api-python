from fastapi import FastAPI
from config.database import engine
from config.database import Base
from routes.producto import router as producto_router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación
app = FastAPI()

# Incluir las rutas desde la carpeta routes
app.include_router(producto_router)
