from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from database.db import Base

# Tabela de associação para relação muitos-para-muitos entre Evento e Convidado
evento_convidado = Table(
    'evento_convidado',
    Base.metadata,
    Column('evento_id', Integer, ForeignKey('evento.id'), primary_key=True),
    Column('convidado_id', Integer, ForeignKey('convidado.id'), primary_key=True)
)

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    data = Column(String(10), nullable=False)  # Exemplo: 'YYYY-MM-DD'
    hora = Column(String(5), nullable=False)  # Exemplo: 'HH:MM'
    local = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    comida = Column(String(255), nullable=True)
    bebida = Column(String(255), nullable=True)
    template_id = Column(Integer, nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)  # FK para Usuario

    # Relacionamentos
    usuario = relationship('Usuario', back_populates='eventos')  # Muitos-para-um com Usuario
    convidados = relationship('Convidado', secondary=evento_convidado, back_populates='eventos')  # Muitos-para-muitos com Convidado
    respostas = relationship('Resposta', back_populates='evento')  # Um-para-muitos com Resposta
