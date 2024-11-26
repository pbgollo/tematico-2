from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Resposta(Base):
    __tablename__ = 'resposta'
    id = Column(Integer, primary_key=True)
    id_convidado = Column(Integer, ForeignKey('convidado.id'), nullable=False)
    id_evento = Column(Integer, ForeignKey('evento.id'), nullable=False)
    confirmacao = Column(Integer, nullable=False)  # Exemplo: 0 para "não", 1 para "sim"
    justificativa = Column(String(500), nullable=True)

    # Relacionamentos
    convidado = relationship('Convidado', back_populates='respostas')  # Um-para-muitos com Convidado
    evento = relationship('Evento', back_populates='respostas')  # Um-para-muitos com Evento
