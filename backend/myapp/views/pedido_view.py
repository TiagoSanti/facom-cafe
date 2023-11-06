from flask_restx import Namespace, Resource, fields
from services.pedido_service import *

# Definindo o namespace
pedido_ns = Namespace('pedidos', description='Operações relacionadas a pedidos')

# Modelo para documentação da API
pedido_model = pedido_ns.model('Pedido', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'data': fields.DateTime(required=True, description='Data do pedido'),
    'status': fields.String(required=True, description='Status do pedido (concluido, cancelado, pendente)')
})

# Recurso para criar pedido
@pedido_ns.route('/criar')
class PedidoCriar(Resource):
    @pedido_ns.expect(pedido_model)
    @pedido_ns.response(201, 'Pedido criado com sucesso.')
    def post(self):
        body = pedido_ns.payload
        pedido = criar_pedido(**body)
        return pedido.to_dict(), 201
    
# Recurso para listar pedidos
@pedido_ns.route('/listar')
class PedidoListar(Resource):
    @pedido_ns.doc('listar_pedidos')
    def get(self):
        pedidos = listar_pedidos()
        return [pedido.to_dict() for pedido in pedidos], 200
    
# Recurso para localizar pedido por ID
@pedido_ns.route('/localizar/<int:id>')
@pedido_ns.param('id', 'Identificador único do pedido')
class PedidoLocalizar(Resource):
    @pedido_ns.doc('localizar_pedido')
    def get(self, id):
        pedido = localizar_pedido(id)
        return pedido.to_dict(), 200
    
# Recurso para listar pedidos de um usuário
@pedido_ns.route('/listar_usuario/<int:id_usuario>')
@pedido_ns.param('id_usuario', 'Identificador único do usuário')
class PedidoListarUsuario(Resource):
    @pedido_ns.doc('listar_pedidos_usuario')
    def get(self, id_usuario):
        pedidos = listar_pedidos_usuario(id_usuario)
        return [pedido.to_dict() for pedido in pedidos], 200
    
# Recurso para excluir pedido
@pedido_ns.route('/excluir/<int:id>')
@pedido_ns.param('id', 'Identificador único do pedido')
class PedidoExcluir(Resource):
    @pedido_ns.doc('excluir_pedido')
    @pedido_ns.response(200, 'Pedido excluído com sucesso.')
    def delete(self, id):
        excluir_pedido(id)
        return {'mensagem': 'Pedido excluído com sucesso'}, 200
    
# Recurso para atualizar pedido
@pedido_ns.route('/atualizar/<int:id>')
@pedido_ns.param('id', 'Identificador único do pedido')
class PedidoAtualizar(Resource):
    @pedido_ns.expect(pedido_model)
    @pedido_ns.response(200, 'Pedido atualizado com sucesso.')
    def put(self, id):
        body = pedido_ns.payload
        pedido = atualizar_pedido(id, **body)
        return pedido.to_dict(), 200
    
# Recurso para cancelar pedido
@pedido_ns.route('/cancelar/<int:id>')
@pedido_ns.param('id', 'Identificador único do pedido')
class PedidoCancelar(Resource):
    @pedido_ns.doc('cancelar_pedido')
    @pedido_ns.response(200, 'Pedido cancelado com sucesso.')
    def put(self, id):
        pedido = cancelar_pedido(id)
        return pedido.to_dict(), 200
    
# Recurso para concluir pedido
@pedido_ns.route('/concluir/<int:id>')
@pedido_ns.param('id', 'Identificador único do pedido')
class PedidoConcluir(Resource):
    @pedido_ns.doc('concluir_pedido')
    @pedido_ns.response(200, 'Pedido concluído com sucesso.')
    def put(self, id):
        pedido = concluir_pedido(id)
        return pedido.to_dict(), 200