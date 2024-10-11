from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255), unique=True)
    senha = Column(String(255))
    
    eventos = relationship("Evento", back_populates="usuario")
