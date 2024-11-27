from dao.UsuarioDao import UsuarioDao
from models.UsuarioModel import Usuario

class UsuarioController:
    def __init__(self, session):
        self.usuario_dao = UsuarioDao(session)

    def autenticar_usuario(self, email: str, senha: str) -> Usuario:
        return self.usuario_dao.autenticar_usuario(email, senha)

    def cadastrar_usuario(self, nome: str, email: str, senha: str) -> Usuario:
        if self.usuario_dao.busca_usuario(email):
            return None 
        return self.usuario_dao.cadastra_usuario(nome, email, senha)
