from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Convidado(Base):
    __tablename__ = 'convidado'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255))
    telefone = Column(String(255))
    
    id_convite = Column(Integer, ForeignKey('convite.id'), unique=True)
    convite = relationship("Convite", back_populates="convidado")    
    convidado_evento = relationship("ConvidadoEvento", back_populates="convidado")