from dao.UsuarioDao import UsuarioDao

class UsuarioController:
    def __init__(self, session):
        self.usuario_dao = UsuarioDao(session)

    def autenticar_usuario(self, email: str, senha: str) -> bool:
        usuario = self.usuario_dao.busca_usuario(email)
        if not usuario:
            return False  # Usuário não encontrado
        return self.usuario_dao.valida_senha(usuario, senha)

    def cadastrar_usuario(self, nome: str, email: str, senha: str) -> bool:
        # Verifica se o e-mail já está cadastrado
        if self.usuario_dao.busca_usuario(email):
            return False  # Usuário já existe
        self.usuario_dao.cadastra_usuario(nome, email, senha)
        return True
