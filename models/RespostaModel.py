from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Resposta(Base):
    __tablename__ = 'resposta'
    id = Column(Integer, primary_key=True)
    confirmacao_de_presenca = Column(Integer)
    texto_justificativa = Column(String(255))
    
    id_convite = Column(Integer, ForeignKey('convite.id'))
    convite = relationship("Convite", back_populates="respostas")