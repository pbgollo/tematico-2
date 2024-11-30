# dao/EventoConvidadoDao.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.EventoConvidadoModel import EventoConvidado

class EventoConvidadoDAO:
    def __init__(self, session: Session):
        self.session = session
    
    def salvar(self, evento_id, convidado_id):
        novo_evento_convidado = EventoConvidado(evento_id=evento_id, convidado_id=convidado_id)
        self.session.add(novo_evento_convidado)
        self.session.commit()

    def contar_convidados(self, evento_id: int) -> int:
        # Conta o número de registros na tabela evento_convidado para o evento_id fornecido
        return self.session.query(func.count(EventoConvidado.id)).filter(EventoConvidado.evento_id == evento_id).scalar()
