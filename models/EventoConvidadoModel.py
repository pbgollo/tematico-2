from sqlalchemy import Column, Integer, ForeignKey
from database.db import Base

class EventoConvidado(Base):
    __tablename__ = 'evento_convidado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey('evento.id'), nullable=False)
    convidado_id = Column(Integer, ForeignKey('convidado.id'), nullable=False)
