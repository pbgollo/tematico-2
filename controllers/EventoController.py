from dao.EventoDao import EventoDao
from dao.ConvidadoDao import ConvidadoDao
from dao.EventoConvidadoDao import EventoConvidadoDAO
from models.EventoModel import Evento

class EventoController:
    def __init__(self, session):
        self.evento_dao = EventoDao(session)
        self.convidado_dao = ConvidadoDao(session)
        self.evento_convidado_dao = EventoConvidadoDAO(session)

    def adicionar_evento(self, nome: str, data: str, hora: str, local: str, endereco: str, id_usuario: int, comida: str = None, bebida: str = None, template_id: int = None) -> dict:
        evento = Evento(
            nome=nome,
            data=data,
            hora=hora,
            local=local,
            endereco=endereco,
            comida=comida,
            bebida=bebida,
            template_id=template_id,
            convite_enviado=0,  
            id_usuario=id_usuario
        )
        
        evento_id = self.evento_dao.cadastra_evento(evento)
        return evento_id

    def listar_eventos(self, id_usuario: int) -> list:
        return self.evento_dao.listar_eventos_por_usuario(id_usuario)

    def excluir_evento(self, evento_id: int) -> dict:
        if self.evento_dao.excluir_evento(evento_id):
            return {"success": True, "message": "Evento excluído com sucesso."}
        return {"success": False, "message": "Evento não encontrado."}
    
    def adicionar_convidados(self, evento_id, emails_convidados):
        for email in emails_convidados:
            convidado = self.convidado_dao.obter_por_email(email)
            if convidado:
                self.evento_convidado_dao.salvar(evento_id, convidado.id)
        # Caso queira retornar algo, como uma confirmação
        return {"success": True, "message": "Convidados adicionados com sucesso!"}
    
    def contar_convidados(self, evento_id: int) -> dict:
        # Recupera o número de convidados associados ao evento
        numero_convidados = self.evento_convidado_dao.contar_convidados(evento_id)
        return numero_convidados
    
    def listar_convidados_por_evento(self, evento_id: int) -> list:
        return self.evento_convidado_dao.listar_convidados(evento_id)

