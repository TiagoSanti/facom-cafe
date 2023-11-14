from flask_restx import Namespace, Resource, fields
from ..services.configuracoes_notificacao_service import *

# Definindo o namespace
configuracoes_notificacao_ns = Namespace('configuracoes_notificacao', description='Operações relacionadas a configurações de notificação')

# Modelo para documentação da API
configuracoes_notificacao_model = configuracoes_notificacao_ns.model('ConfiguracoesNotificacao', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'receber_email': fields.Boolean(required=True, description='Receber notificações por e-mail'),
    'receber_sms': fields.Boolean(required=True, description='Receber notificações por SMS'),
    'frequencia': fields.String(required=True, description='Frequência das notificações', enum=['diário', 'semanal', 'mensal'])
})

# Recurso para criar configuracoes_notificacao
@configuracoes_notificacao_ns.route('/criar')
class ConfiguracoesNotificacaoCriar(Resource):
    @configuracoes_notificacao_ns.expect(configuracoes_notificacao_model)
    @configuracoes_notificacao_ns.response(201, 'ConfiguracoesNotificacao criado com sucesso.')
    def post(self):
        body = configuracoes_notificacao_ns.payload
        configuracoes_notificacao = criar_configuracoes_notificacao(**body)
        return configuracoes_notificacao.to_dict(), 201
    
# Recurso para listar configuracoes_notificacoes
@configuracoes_notificacao_ns.route('/listar')
class ConfiguracoesNotificacaoListar(Resource):
    @configuracoes_notificacao_ns.doc('listar_configuracoes_notificacoes')
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacoes listados com sucesso.')
    def get(self):
        configuracoes_notificacoes = listar_configuracoes_notificacoes()
        return [configuracoes_notificacao.to_dict() for configuracoes_notificacao in configuracoes_notificacoes], 200
    
# Recurso para localizar configuracoes_notificacao por ID
@configuracoes_notificacao_ns.route('/localizar/<int:id>')
@configuracoes_notificacao_ns.param('id', 'Identificador único da configuração de notificação')
class ConfiguracoesNotificacaoLocalizar(Resource):
    @configuracoes_notificacao_ns.doc('localizar_configuracoes_notificacao')
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacao localizado com sucesso.')
    def get(self, id):
        configuracoes_notificacao = localizar_configuracoes_notificacao(id)
        return configuracoes_notificacao.to_dict(), 200
    
# Recurso para localizar configuracoes_notificacao por ID de usuário
@configuracoes_notificacao_ns.route('/localizar/<int:id_usuario>')
@configuracoes_notificacao_ns.param('id_usuario', 'Identificador único do usuário')
class ConfiguracoesNotificacaoLocalizarPorUsuario(Resource):
    @configuracoes_notificacao_ns.doc('localizar_configuracoes_notificacao_por_usuario')
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacao localizado com sucesso.')
    def get(self, id_usuario):
        configuracoes_notificacao = localizar_configuracoes_notificacao_por_usuario(id_usuario)
        return configuracoes_notificacao.to_dict(), 200
    
# Recurso para excluir configuracoes_notificacao
@configuracoes_notificacao_ns.route('/excluir/<int:id>')
@configuracoes_notificacao_ns.param('id', 'Identificador único da configuração de notificação')
class ConfiguracoesNotificacaoExcluir(Resource):
    @configuracoes_notificacao_ns.doc('excluir_configuracoes_notificacao')
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacao excluído com sucesso.')
    def delete(self, id):
        excluir_configuracoes_notificacao(id)
        return {'mensagem': 'ConfiguracoesNotificacao excluído com sucesso'}, 200
    
# Recurso para atualizar configuracoes_notificacao
@configuracoes_notificacao_ns.route('/atualizar/<int:id>')
@configuracoes_notificacao_ns.param('id', 'Identificador único da configuração de notificação')
class ConfiguracoesNotificacaoAtualizar(Resource):
    @configuracoes_notificacao_ns.expect(configuracoes_notificacao_model)
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacao atualizado com sucesso.')
    def put(self, id):
        body = configuracoes_notificacao_ns.payload
        configuracoes_notificacao = atualizar_configuracoes_notificacao(id, **body)
        return configuracoes_notificacao.to_dict(), 200
    
# Recurso para atualizar configuracoes_notificacao por ID de usuário
@configuracoes_notificacao_ns.route('/atualizar/<int:id_usuario>')
@configuracoes_notificacao_ns.param('id_usuario', 'Identificador único do usuário')
class ConfiguracoesNotificacaoAtualizarPorUsuario(Resource):
    @configuracoes_notificacao_ns.expect(configuracoes_notificacao_model)
    @configuracoes_notificacao_ns.response(200, 'ConfiguracoesNotificacao atualizado com sucesso.')
    def put(self, id_usuario):
        body = configuracoes_notificacao_ns.payload
        configuracoes_notificacao = atualizar_configuracoes_notificacao_por_usuario(id_usuario, **body)
        return configuracoes_notificacao.to_dict(), 200