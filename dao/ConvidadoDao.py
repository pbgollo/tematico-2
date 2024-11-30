from sqlalchemy.orm import Session
from models.ConvidadoModel import Convidado
from sqlalchemy.exc import NoResultFound

class ConvidadoDao:
    def __init__(self, session: Session):
        self.session = session

    def cadastra_convidado(self, nome: str, email: str, id_usuario: int) -> Convidado:
        novo_convidado = Convidado(nome=nome, email=email, id_usuario=id_usuario)
        self.session.add(novo_convidado)
        self.session.commit()
        return novo_convidado

    def busca_convidado_por_email(self, email: str) -> Convidado:
        try:
            return self.session.query(Convidado).filter_by(email=email).one()
        except NoResultFound:
            return None

    def listar_convidados_por_usuario(self, id_usuario: int) -> list:
        return self.session.query(Convidado).filter_by(id_usuario=id_usuario).all()

    def excluir_convidado(self, convidado_id: int) -> bool:
        try:
            convidado = self.session.query(Convidado).filter_by(id=convidado_id).one()
            self.session.delete(convidado)
            self.session.commit()
            return True
        except NoResultFound:
            return False
        
    def obter_por_email(self, email):
        return self.session.query(Convidado).filter_by(email=email).first()
