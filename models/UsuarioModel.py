from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefone = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)

    # Relacionamentos
    convidados = relationship('Convidado', back_populates='usuario')  # Um-para-muitos com Convidado
    eventos = relationship('Evento', back_populates='usuario')  # Um-para-muitos com Evento
