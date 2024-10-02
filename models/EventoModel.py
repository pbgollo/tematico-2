from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    data_hora = Column(DateTime)
    local = Column(String(255))
    descricao = Column(String(255))
    caminho_arquivo_midia = Column(String(255))
    
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="eventos")    
    cardapio = relationship("Cardapio", back_populates="evento")
    convites = relationship("Convite", back_populates="evento")
    convidado_evento = relationship("ConvidadoEvento", back_populates="evento")
