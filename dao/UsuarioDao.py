from sqlalchemy.orm import Session
from models.UsuarioModel import Usuario
from sqlalchemy.exc import NoResultFound

class UsuarioDao:
    def __init__(self, session: Session):
        self.session = session

    def busca_usuario(self, email: str) -> Usuario:
        try:
            usuario = self.session.query(Usuario).filter_by(email=email).one()
            return usuario
        except NoResultFound:
            return None

    def valida_senha(self, usuario: Usuario, senha: str) -> bool:
        return usuario.senha == senha  # Aqui você pode melhorar usando hashing de senha

    def cadastra_usuario(self, nome: str, email: str, senha: str) -> Usuario:
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        self.session.add(novo_usuario)
        self.session.commit()
        return novo_usuario
