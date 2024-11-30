from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    data = Column(String(10), nullable=False)
    hora = Column(String(5), nullable=False)
    local = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    comida = Column(String(255), nullable=True)
    bebida = Column(String(255), nullable=True)
    template_id = Column(Integer, nullable=True)
    convite_enviado = Column(Integer, nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='eventos')
    convidados = relationship("Convidado", secondary='evento_convidado', back_populates="eventos")
