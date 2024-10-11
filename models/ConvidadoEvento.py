from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class ConvidadoEvento(Base):
    __tablename__ = 'convidado_evento'
    id_evento = Column(Integer, ForeignKey('evento.id'), primary_key=True)
    id_convidado = Column(Integer, ForeignKey('convidado.id'), primary_key=True)
    
    evento = relationship("Evento", back_populates="convidado_evento")
    convidado = relationship("Convidado", back_populates="convidado_evento")
