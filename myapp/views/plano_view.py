from flask_restx import Namespace, Resource, fields
from services.plano_service import criar_plano, listar_planos, localizar_plano, excluir_plano, atualizar_plano

# Definindo o namespace
plano_ns = Namespace('planos', description='Operações relacionadas a planos')

# Modelo para documentação da API
plano_model = plano_ns.model('Plano', {
    'nome': fields.String(required=True, description='Nome do plano'),
    'descricao': fields.String(required=True, description='Descrição do plano'),
    'preco': fields.Float(required=True, description='Preço do plano'),
    'duracao': fields.Integer(required=True, description='Duração do plano')
})

# Recurso para criar plano
@plano_ns.route('/criar')
class PlanoCriar(Resource):
    @plano_ns.expect(plano_model)
    @plano_ns.response(201, 'Plano criado com sucesso.')
    def post(self):
        body = plano_ns.payload
        plano = criar_plano(**body)
        return plano.to_dict(), 201
    
# Recurso para listar planos
@plano_ns.route('/listar')
class PlanoListar(Resource):
    @plano_ns.doc('listar_planos')
    def get(self):
        planos = listar_planos()
        return [plano.to_dict() for plano in planos], 200
    
# Recurso para localizar plano por ID
@plano_ns.route('/localizar/<int:id>')
@plano_ns.param('id', 'Identificador único do plano')
class PlanoLocalizar(Resource):
    @plano_ns.doc('localizar_plano')
    def get(self, id):
        plano = localizar_plano(id)
        return plano.to_dict(), 200
    
# Recurso para excluir plano
@plano_ns.route('/excluir/<int:id>')
@plano_ns.param('id', 'Identificador único do plano')
class PlanoExcluir(Resource):
    @plano_ns.doc('excluir_plano')
    @plano_ns.response(200, 'Plano excluído com sucesso.')
    def delete(self, id):
        excluir_plano(id)
        return {'mensagem': 'Plano excluído com sucesso'}, 200

# Recurso para atualizar plano
@plano_ns.route('/atualizar/<int:id>')
@plano_ns.param('id', 'Identificador único do plano')
class PlanoAtualizar(Resource):
    @plano_ns.expect(plano_model)
    @plano_ns.response(200, 'Plano atualizado com sucesso.')
    def put(self, id):
        body = plano_ns.payload
        plano = atualizar_plano(id, **body)
        return plano.to_dict(), 200