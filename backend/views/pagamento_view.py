from flask_restx import Namespace, Resource, fields
from ..services.pagamento_service import *

# Definindo o namespace
pagamento_ns = Namespace('pagamentos', description='Operações relacionadas a pagamentos')

# Modelo para documentação da API
pagamento_model = pagamento_ns.model('Pagamento', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'id_plano': fields.Integer(required=True, description='ID do plano'),
    'data': fields.Date(required=True, description='Data do pagamento'),
    'valor': fields.Float(required=True, description='Valor do pagamento'),
    'metodo': fields.String(required=True, description='Método de pagamento')
})

# Recurso para criar pagamento
@pagamento_ns.route('/criar')
class PagamentoCriar(Resource):
    @pagamento_ns.expect(pagamento_model)
    @pagamento_ns.response(201, 'Pagamento criado com sucesso.')
    def post(self):
        body = pagamento_ns.payload
        pagamento = criar_pagamento(**body)
        return pagamento.to_dict(), 201
    
# Recurso para listar pagamentos
@pagamento_ns.route('/listar')
class PagamentoListar(Resource):
    @pagamento_ns.doc('listar_pagamentos')
    def get(self):
        pagamentos = listar_pagamentos()
        return [pagamento.to_dict() for pagamento in pagamentos], 200
    
# Recurso para localizar pagamento por ID
@pagamento_ns.route('/localizar/<int:id>')
@pagamento_ns.param('id', 'Identificador único do pagamento')
class PagamentoLocalizar(Resource):
    @pagamento_ns.doc('localizar_pagamento')
    def get(self, id):
        pagamento = localizar_pagamento(id)
        return pagamento.to_dict(), 200
    
# Recurso para excluir pagamento
@pagamento_ns.route('/excluir/<int:id>')
@pagamento_ns.param('id', 'Identificador único do pagamento')
class PagamentoExcluir(Resource):
    @pagamento_ns.doc('excluir_pagamento')
    @pagamento_ns.response(200, 'Pagamento excluído com sucesso.')
    def delete(self, id):
        excluir_pagamento(id)
        return {'mensagem': 'Pagamento excluído com sucesso'}, 200

# Recurso para atualizar pagamento
@pagamento_ns.route('/atualizar/<int:id>')
@pagamento_ns.param('id', 'Identificador único do pagamento')
class PagamentoAtualizar(Resource):
    @pagamento_ns.expect(pagamento_model)
    @pagamento_ns.response(200, 'Pagamento atualizado com sucesso.')
    def put(self, id):
        body = pagamento_ns.payload
        pagamento = atualizar_pagamento(id, **body)
        return pagamento.to_dict(), 200

# Recurso para listar pagamentos por usuário
@pagamento_ns.route('/listar_por_usuario/<int:id_usuario>')
@pagamento_ns.param('id_usuario', 'Identificador único do usuário')
class PagamentoListarPorUsuario(Resource):
    @pagamento_ns.doc('listar_pagamentos_por_usuario')
    def get(self, id_usuario):
        pagamentos = listar_pagamentos_por_usuario(id_usuario)
        return [pagamento.to_dict() for pagamento in pagamentos], 200
    
# Recurso para listar pagamentos por período
@pagamento_ns.route('/listar_por_periodo/<string:data_inicio>/<string:data_fim>')
@pagamento_ns.param('data_inicio', 'Data de início do período')
@pagamento_ns.param('data_fim', 'Data de fim do período')
class PagamentoListarPorPeriodo(Resource):
    @pagamento_ns.doc('listar_pagamentos_por_periodo')
    def get(self, data_inicio, data_fim):
        pagamentos = listar_pagamentos_por_periodo(data_inicio, data_fim)
        return [pagamento.to_dict() for pagamento in pagamentos], 200
    
# Recurso para listar pagamentos por período e usuário
@pagamento_ns.route('/listar_por_periodo_usuario/<int:id_usuario>/<string:data_inicio>/<string:data_fim>')
@pagamento_ns.param('id_usuario', 'Identificador único do usuário')
@pagamento_ns.param('data_inicio', 'Data de início do período')
@pagamento_ns.param('data_fim', 'Data de fim do período')
class PagamentoListarPorPeriodoUsuario(Resource):
    @pagamento_ns.doc('listar_pagamentos_por_periodo_usuario')
    def get(self, id_usuario, data_inicio, data_fim):
        pagamentos = listar_pagamentos_por_periodo_usuario(id_usuario, data_inicio, data_fim)
        return [pagamento.to_dict() for pagamento in pagamentos], 200