from sqlalchemy.orm import Session
from models.ConvidadoModel import Convidado
from sqlalchemy.exc import NoResultFound

class ConvidadoDao:
    def __init__(self, session: Session):
        self.session = session

    def cadastra_convidado(self, nome: str, email: str) -> Convidado:
        novo_convidado = Convidado(nome=nome, email=email)
        self.session.add(novo_convidado)
        self.session.commit()
        return novo_convidado

    def busca_convidado_por_email(self, email: str) -> Convidado:
        try:
            convidado = self.session.query(Convidado).filter_by(email=email).one()
            return convidado
        except NoResultFound:
            return None

    def listar_convidados(self) -> list:
        return self.session.query(Convidado).all()

    def excluir_convidado(self, convidado_id: int) -> None:
        try:
            convidado = self.session.query(Convidado).filter_by(id=convidado_id).one()
            self.session.delete(convidado)
            self.session.commit()
        except NoResultFound:
            pass
