from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Convite(Base):
    __tablename__ = 'convite'
    id = Column(Integer, primary_key=True)
    texto_do_email = Column(String(255))
    url_de_confirmacao = Column(String(255))
    caminho_arquivo_midia = Column(String(255))
    
    id_evento = Column(Integer, ForeignKey('evento.id'))
    evento = relationship("Evento", back_populates="convites")    
    id_template_convite = Column(Integer, ForeignKey('template_convite.id'))
    template_convite = relationship("TemplateConvite", back_populates="convites")    
    convidado = relationship("Convidado", back_populates="convite")
    respostas = relationship("Resposta", back_populates="convite")
