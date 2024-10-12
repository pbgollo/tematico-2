from dao.ConvidadoDao import ConvidadoDao

class ConvidadoController:
    def __init__(self, session):
        self.convidado_dao = ConvidadoDao(session)

    def cadastrar_convidado(self, nome: str, email: str) -> bool:
        if self.convidado_dao.busca_convidado_por_email(email):
            return False
        self.convidado_dao.cadastra_convidado(nome, email)
        return True

    def listar_convidados(self) -> list:
        return self.convidado_dao.listar_convidados()

    def excluir_convidado(self, convidado_id: int) -> None:
        self.convidado_dao.excluir_convidado(convidado_id)
