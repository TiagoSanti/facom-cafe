from flask_restx import Namespace, Resource, fields
from services.log_service import *

# Definindo o namespace
log_ns = Namespace('log', description='Operações relacionadas a logs')

# Modelo para documentação da API
log_model = log_ns.model('Log', {
    'id': fields.Integer(required=True, description='ID do log'),
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'tabela_modificada': fields.String(required=True, description='Tabela modificada'),
    'modificacao': fields.String(required=True, description='Tipo de modificação'),
    'data': fields.Date(required=True, description='Data da modificação'),
    'detalhes': fields.String(required=True, description='Detalhes da modificação')
})

# Recurso para listar logs
@log_ns.route('/listar')
class LogListar(Resource):
    @log_ns.doc('listar_logs')
    def get(self):
        logs = listar_logs()
        return [log.to_dict() for log in logs], 200
    
# Recurso para localizar log por ID
@log_ns.route('/localizar/<int:id>')
@log_ns.param('id', 'Identificador único do log')
class LogLocalizar(Resource):
    @log_ns.doc('localizar_log')
    def get(self, id):
        log = localizar_log(id)
        return log.to_dict(), 200
    
# Recurso para listar logs por tabela
@log_ns.route('/listar/<string:tabela>')
@log_ns.param('tabela', 'Nome da tabela')
class LogListarPorTabela(Resource):
    @log_ns.doc('listar_logs_por_tabela')
    def get(self, tabela):
        logs = listar_logs_por_tabela(tabela)
        return [log.to_dict() for log in logs], 200
    
# Recurso para listar logs por modificação
@log_ns.route('/listar/<string:modificacao>')
@log_ns.param('modificacao', 'Tipo de modificação')
class LogListarPorModificacao(Resource):
    @log_ns.doc('listar_logs_por_modificacao')
    def get(self, modificacao):
        logs = listar_logs_por_modificacao(modificacao)
        return [log.to_dict() for log in logs], 200

# Recurso para listar logs por intervalo de data
@log_ns.route('/listar/<string:data_inicio>/<string:data_fim>')
@log_ns.param('data_inicio', 'Data de início')
@log_ns.param('data_fim', 'Data de fim')
class LogListarPorIntervaloData(Resource):
    @log_ns.doc('listar_logs_por_intervalo_data')
    def get(self, data_inicio, data_fim):
        logs = listar_logs_por_intervalo_data(data_inicio, data_fim)
        return [log.to_dict() for log in logs], 200