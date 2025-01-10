from sqlalchemy import Column, Integer, String, Date, Enum, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False, index=True, comment="Correo único")
    password_hash = Column(String(255), nullable=False, comment="Contraseña encriptada")
    role = Column(String(30), nullable=False, default="desactivado", comment="Rol del usuario")
    