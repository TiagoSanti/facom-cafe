from flask_restx import Namespace, Resource, fields
from ..services.pedido_produto_service import *

# Definindo o namespace
pedido_produto_ns = Namespace('pedidos_produtos', description='Operações relacionadas a pedidos de produtos')

# Modelo para documentação da API
pedido_produto_model = pedido_produto_ns.model('PedidoProduto', {
    'id_pedido': fields.Integer(required=True, description='ID do pedido'),
    'id_produto': fields.Integer(required=True, description='ID do produto'),
    'quantidade': fields.Integer(required=True, description='Quantidade do produto'),
    'valor': fields.Float(required=True, description='Valor do produto')
})

# Recurso para criar pedido_produto
@pedido_produto_ns.route('/criar')
class PedidoProdutoCriar(Resource):
    @pedido_produto_ns.expect(pedido_produto_model)
    @pedido_produto_ns.response(201, 'PedidoProduto criado com sucesso.')
    def post(self):
        body = pedido_produto_ns.payload
        pedido_produto = criar_pedido_produto(**body)
        return pedido_produto.to_dict(), 201
    
# Recurso para listar pedidos_produtos
@pedido_produto_ns.route('/listar')
class PedidoProdutoListar(Resource):
    @pedido_produto_ns.doc('listar_pedidos_produtos')
    def get(self):
        pedidos_produtos = listar_pedidos_produtos()
        return [pedido_produto.to_dict() for pedido_produto in pedidos_produtos], 200
    
# Recurso para localizar pedido_produto por ID
@pedido_produto_ns.route('/localizar/<int:id_pedido>/<int:id_produto>')
@pedido_produto_ns.param('id_pedido', 'Identificador único do pedido')
@pedido_produto_ns.param('id_produto', 'Identificador único do produto')
class PedidoProdutoLocalizar(Resource):
    @pedido_produto_ns.doc('localizar_pedido_produto')
    def get(self, id_pedido, id_produto):
        pedido_produto = localizar_pedido_produto(id_pedido, id_produto)
        return pedido_produto.to_dict(), 200
    
# Recurso para excluir pedido_produto
@pedido_produto_ns.route('/excluir/<int:id_pedido>/<int:id_produto>')
@pedido_produto_ns.param('id_pedido', 'Identificador único do pedido')
@pedido_produto_ns.param('id_produto', 'Identificador único do produto')
class PedidoProdutoExcluir(Resource):
    @pedido_produto_ns.doc('excluir_pedido_produto')
    @pedido_produto_ns.response(200, 'PedidoProduto excluído com sucesso.')
    def delete(self, id_pedido, id_produto):
        excluir_pedido_produto(id_pedido, id_produto)
        return {'mensagem': 'PedidoProduto excluído com sucesso'}, 200
    
# Recurso para atualizar pedido_produto
@pedido_produto_ns.route('/atualizar/<int:id_pedido>/<int:id_produto>')
@pedido_produto_ns.param('id_pedido', 'Identificador único do pedido')
@pedido_produto_ns.param('id_produto', 'Identificador único do produto')
class PedidoProdutoAtualizar(Resource):
    @pedido_produto_ns.expect(pedido_produto_model)
    @pedido_produto_ns.response(200, 'PedidoProduto atualizado com sucesso.')
    def put(self, id_pedido, id_produto):
        body = pedido_produto_ns.payload
        pedido_produto = atualizar_pedido_produto(id_pedido, id_produto, **body)
        return pedido_produto.to_dict(), 200