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

    def valida_senha(self, usuario: Usuario, senha: str) -> Usuario:
        if usuario.senha == senha:  # Aqui você pode implementar hashing para maior segurança
            return usuario
        return None

    def autenticar_usuario(self, email: str, senha: str) -> Usuario:
        usuario = self.busca_usuario(email)
        if usuario and self.valida_senha(usuario, senha):
            return usuario
        return None

    def cadastra_usuario(self, nome: str, email: str, telefone: str, senha: str) -> Usuario:
        novo_usuario = Usuario(nome=nome, email=email, telefone=telefone, senha=senha)
        self.session.add(novo_usuario)
        self.session.commit()
        return novo_usuario
