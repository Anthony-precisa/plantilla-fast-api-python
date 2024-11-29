from collections import OrderedDict
from sqlalchemy import Column, Integer, String
from config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion  = Column(String, index=True)
    precio = Column(Integer)

    def to_dict(self):
        # Usamos OrderedDict para garantizar el orden
        return OrderedDict([
            ("id", self.id),
            ("descripcion", self.nombre),
            ("precio", self.precio)
        ])
