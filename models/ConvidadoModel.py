from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Convidado(Base):
    __tablename__ = 'convidado'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='convidados')
    eventos = relationship("Evento", secondary='evento_convidado', back_populates="convidados")
