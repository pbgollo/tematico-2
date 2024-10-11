from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Cardapio(Base):
    __tablename__ = 'cardapio'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(255))
    nome = Column(String(255))
    caminho_arquivo_midia = Column(String(255))
    
    id_evento = Column(Integer, ForeignKey('evento.id'))
    evento = relationship("Evento", back_populates="cardapio")
