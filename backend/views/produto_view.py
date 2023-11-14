from flask_restx import Namespace, Resource, fields
from ..services.produto_service import *

# Definindo o namespace
produto_ns = Namespace('produtos', description='Operações relacionadas a produtos')

# Modelo para documentação da API
produto_model = produto_ns.model('Produto', {
    'nome': fields.String(required=True, description='Nome do produto'),
    'preco': fields.Float(required=True, description='Preço do produto'),
    'qtd_estoque': fields.Integer(required=True, description='Quantidade em estoque do produto'),
    'descricao': fields.String(required=False, description='Descrição do produto')
})

# Recurso para criar produto
@produto_ns.route('/criar')
class ProdutoCriar(Resource):
    @produto_ns.expect(produto_model)
    @produto_ns.response(201, 'Produto criado com sucesso.')
    def post(self):
        body = produto_ns.payload
        produto = criar_produto(**body)
        return produto.to_dict(), 201
    
# Recurso para listar produtos
@produto_ns.route('/listar')
class ProdutoListar(Resource):
    @produto_ns.doc('listar_produtos')
    @produto_ns.response(200, 'Produtos listados com sucesso.')
    def get(self):
        produtos = listar_produtos()
        return [produto.to_dict() for produto in produtos], 200
    
# Recurso para localizar produto por ID
@produto_ns.route('/localizar/<int:id>')
@produto_ns.param('id', 'Identificador único do produto')
class ProdutoLocalizar(Resource):
    @produto_ns.doc('localizar_produto')
    @produto_ns.response(200, 'Produto localizado com sucesso.')
    def get(self, id):
        produto = localizar_produto(id)
        return produto.to_dict(), 200
    
# Recurso para excluir produto
@produto_ns.route('/excluir/<int:id>')
@produto_ns.param('id', 'Identificador único do produto')
class ProdutoExcluir(Resource):
    @produto_ns.doc('excluir_produto')
    @produto_ns.response(200, 'Produto excluído com sucesso.')
    def delete(self, id):
        excluir_produto(id)
        return {'mensagem': 'Produto excluído com sucesso'}, 200
    
# Recurso para atualizar produto
@produto_ns.route('/atualizar/<int:id>')
@produto_ns.param('id', 'Identificador único do produto')
class ProdutoAtualizar(Resource):
    @produto_ns.expect(produto_model)
    @produto_ns.response(200, 'Produto atualizado com sucesso.')
    def put(self, id):
        body = produto_ns.payload
        produto = atualizar_produto(id, **body)
        return produto.to_dict(), 200
    
# Recurso para adicionar estoque
@produto_ns.route('/adicionar_estoque/<int:id>/<int:qtd>')
@produto_ns.param('id', 'Identificador único do produto')
@produto_ns.param('qtd', 'Quantidade a ser adicionada ao estoque')
class ProdutoAdicionarEstoque(Resource):
    @produto_ns.doc('adicionar_estoque')
    @produto_ns.response(200, 'Estoque adicionado com sucesso.')
    def put(self, id, qtd):
        produto = adicionar_estoque(id, qtd)
        return produto.to_dict(), 200
    
# Recurso para remover estoque
@produto_ns.route('/remover_estoque/<int:id>/<int:qtd>')
@produto_ns.param('id', 'Identificador único do produto')
@produto_ns.param('qtd', 'Quantidade a ser removida do estoque')
class ProdutoRemoverEstoque(Resource):
    @produto_ns.doc('remover_estoque')
    @produto_ns.response(200, 'Estoque removido com sucesso.')
    def put(self, id, qtd):
        produto = remover_estoque(id, qtd)
        return produto.to_dict(), 200