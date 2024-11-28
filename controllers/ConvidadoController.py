from dao.ConvidadoDao import ConvidadoDao

class ConvidadoController:
    def __init__(self, session):
        self.convidado_dao = ConvidadoDao(session)

    def cadastrar_convidado(self, nome: str, email: str, id_usuario: int) -> bool:
        if self.convidado_dao.busca_convidado_por_email(email):
            return False  # E-mail já cadastrado
        self.convidado_dao.cadastra_convidado(nome, email, id_usuario)
        return True

    def listar_convidados(self, id_usuario: int) -> list:
        return self.convidado_dao.listar_convidados_por_usuario(id_usuario)

    def excluir_convidado(self, convidado_id: int) -> bool:
        return self.convidado_dao.excluir_convidado(convidado_id)
