from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class TemplateConvite(Base):
    __tablename__ = 'template_convite'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    descricao = Column(String(255))
    texto_do_template = Column(String(255))
    caminho_arquivo_midia = Column(String(255))
    
    convites = relationship("Convite", back_populates="template_convite")