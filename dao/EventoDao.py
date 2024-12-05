from sqlalchemy.orm import Session
from models.EventoModel import Evento
from models.ConvidadoModel import Convidado
from sqlalchemy.exc import NoResultFound

class EventoDao:
    def __init__(self, session: Session):
        self.session = session

    def cadastra_evento(self, evento: Evento) -> int:  # Retorna o ID do evento
        self.session.add(evento)
        self.session.commit()  # Realiza o commit para salvar no banco
        self.session.refresh(evento)  # Atualiza o objeto para garantir que o ID foi gerado
        return evento.id  # Retorna o ID do evento


    def busca_evento_por_id(self, evento_id: int) -> Evento:
        try:
            return self.session.query(Evento).filter_by(id=evento_id).one()
        except NoResultFound:
            return None

    def listar_eventos_por_usuario(self, id_usuario: int) -> list:
        return self.session.query(Evento).filter_by(id_usuario=id_usuario).all()

    def excluir_evento(self, evento_id: int) -> bool:
        try:
            evento = self.session.query(Evento).filter_by(id=evento_id).one()
            self.session.delete(evento)
            self.session.commit()
            return True
        except NoResultFound:
            return False

    def adicionar_convidado_ao_evento(self, evento_id: int, convidado_id: int) -> bool:
        try:
            evento = self.session.query(Evento).filter_by(id=evento_id).one()
            evento.convidados.append(self.session.query(Convidado).filter_by(id=convidado_id).one())
            self.session.commit()
            return True
        except NoResultFound:
            return False
        
    def editar_evento(self, evento_id: int, **dados_atualizados) -> bool:
        try:
            evento = self.session.query(Evento).filter_by(id=evento_id).one()
            for chave, valor in dados_atualizados.items():
                if hasattr(evento, chave):
                    setattr(evento, chave, valor)

            self.session.commit()
            return True
        except NoResultFound:
            return False

