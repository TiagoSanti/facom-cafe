from flask import request
from flask_restx import Namespace, Resource, fields
from ..services.plano_service import *
from ..models import Plano

# Definindo o namespace
plano_ns = Namespace('planos', description='Operações relacionadas a planos')

# Modelo para documentação da API
plano_model = plano_ns.model('Plano', {
    'nome': fields.String(required=True, description='Nome do plano'),
    'descricao': fields.String(required=True, description='Descrição do plano'),
    'preco': fields.Float(required=True, description='Preço do plano'),
})

# Recurso para criar e listar planos
@plano_ns.route('/')
class PlanoCriarListar(Resource):
    @plano_ns.expect(plano_model, validate=True)
    @plano_ns.doc('criar_plano',
        description='Cria um novo plano com nome, descrição e preço.',
        responses={
            201: 'Plano criado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o nome já estiver em uso.'
        }
    )
    def post(self):
        dados = request.json
        res = criar_plano(**dados)

        if isinstance(res, Plano):
            return {'mensagem': 'Plano criado com sucesso',
                    'plano': res.to_dict()}, 201
        else:
            plano_ns.abort(400, res)

    @plano_ns.doc('listar_planos',
        description='Lista todos os planos cadastrados.',
        responses={
            200: 'Planos listados com sucesso.'
        }
    )
    def get(self):
        planos = listar_planos()
        return {'planos': [plano.to_dict() for plano in planos]}, 200

# Recurso para localizar, atualizar e excluir plano por ID
@plano_ns.route('/<int:id>')
@plano_ns.param('id', 'Identificador único do plano')
class PlanoResource(Resource):
    @plano_ns.doc('localizar_plano',
        description='Localiza um plano pelo ID.',
        param = {
            'id': 'ID único representando o plano.'
        },
        responses={
            200: 'Plano localizado com sucesso.',
            404: 'Plano não encontrado.'
        }
    )
    def get(self, id):
        res = localizar_plano(id)

        if res is not None:
            return {'plano': res.to_dict()}, 200
        else:
            plano_ns.abort(404, 'Plano não encontrado')

    @plano_ns.expect(plano_model, validate=True)
    @plano_ns.doc('atualizar_plano',
        description='Atualiza um plano pelo ID.',
        param = {
            'id': 'ID único representando o plano.'
        },
        responses={
            200: 'Plano atualizado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o nome já estiver em uso.',
            404: 'Plano não encontrado.'
        }
    )
    def put(self, id):
        dados = request.json
        res = atualizar_plano(id, **dados)

        if isinstance(res, Plano):
            return {'mensagem': 'Plano atualizado com sucesso',
                    'plano': res.to_dict()}, 200
        else:
            plano_ns.abort(400, res)

    @plano_ns.doc('excluir_plano',
        description='Exclui um plano pelo ID.',
        params={
            'id': 'ID único representando o plano.'
        },
        responses={
            200: 'Plano excluído com sucesso.',
            404: 'Plano não encontrado.'
        }
    )
    def delete(self, id):
        res = excluir_plano(id)

        if isinstance(res, Plano):
            return {'mensagem': 'Plano excluído com sucesso',
                    'plano': res.to_dict()}, 200
        else:
            plano_ns.abort(404, 'Plano não encontrado')