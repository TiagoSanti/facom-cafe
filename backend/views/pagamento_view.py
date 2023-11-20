from flask import request
from flask_restx import Namespace, Resource, fields

import backend
from ..services.pagamento_service import *
from ..models import Pagamento

# Definindo o namespace
pagamento_ns = Namespace('pagamentos', description='Operações relacionadas a pagamentos')

# Modelo para documentação da API
pagamento_create_model = pagamento_ns.model('Pagamento', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'id_assinatura': fields.Integer(required=True, description='ID da assinatura'),
    'metodo': fields.String(required=True, description='Método de pagamento')
})

pagamento_model = pagamento_ns.inherit('PagamentoFull', pagamento_create_model, {
    'data': fields.Date(description='Data do pagamento'),
    'valor': fields.Float(description='Valor do pagamento')
})

# Recurso para criar e listar pagamentos
@pagamento_ns.route('/')
class PagamentoCriarListar(Resource):
    @pagamento_ns.expect(pagamento_create_model, validate=True)
    @pagamento_ns.doc('criar_pagamento',
        description='Cria um novo pagamento com ID do usuário, ID da assinatura, data, valor e método.',
        responses={
            201: 'Pagamento criado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o método não for válido',
            404: 'Usuário ou assinatura não encontrados.'
        }
    )
    def post(self):
        dados = request.json
        res = criar_pagamento(**dados)

        if isinstance(res, backend.models.Pagamento):
            return {'mensagem': 'Pagamento criado com sucesso',
                    'pagamento': res.to_dict()}, 201
        else:
            pagamento_ns.abort(400, res)

    @pagamento_ns.doc('listar_pagamentos',
        description='Lista todos os pagamentos cadastrados.',
        responses={
            200: 'Pagamentos listados com sucesso.'
        }
    )
    def get(self):
        pagamentos = listar_pagamentos()
        return {'pagamentos': [pagamento.to_dict() for pagamento in pagamentos]}, 200

# Recurso para localizar, atualizar e excluir pagamento por ID
@pagamento_ns.route('/<int:id>')
@pagamento_ns.param('id', 'Identificador único do pagamento')
class Pagamento(Resource):
    @pagamento_ns.doc('localizar_pagamento',
        description='Localiza um pagamento pelo ID.',
        responses={
            200: 'Pagamento encontrado com sucesso.',
            404: 'Pagamento não encontrado.'
        }
    )
    def get(self, id):
        pagamento = localizar_pagamento(id)
        if pagamento:
            return {'pagamento': pagamento.to_dict()}, 200
        else:
            pagamento_ns.abort(404, 'Pagamento não encontrado')

    @pagamento_ns.expect(pagamento_model, validate=True)
    @pagamento_ns.doc('atualizar_pagamento',
        description='Atualiza um pagamento pelo ID.',
        responses={
            200: 'Pagamento atualizado com sucesso.',
            400: 'Requisição inválida.',
            404: 'Pagamento não encontrado.'
        }
    )
    def put(self, id):
        dados = request.json
        res = atualizar_pagamento(id, **dados)

        if isinstance(res, backend.models.Pagamento):
            print('Pagamento atualizado com sucesso')
            return {'mensagem': 'Pagamento atualizado com sucesso',
                    'pagamento': res.to_dict()}, 200
        elif isinstance(res, str) and res.contains('válido'):
            print('Requisição inválida')
            pagamento_ns.abort(400, res)
        else:
            print('Pagamento não encontrado')
            pagamento_ns.abort(404, res)
 
    @pagamento_ns.doc('excluir_pagamento',
        description='Exclui um pagamento pelo ID.',
        responses={
            200: 'Pagamento excluído com sucesso.',
            404: 'Pagamento não encontrado.'
        }
    )
    def delete(self, id):
        res = excluir_pagamento(id)

        if isinstance(res, backend.models.Pagamento):
            return {'mensagem': 'Pagamento excluído com sucesso',
                    'pagamento': res.to_dict()}, 200
        else:
            pagamento_ns.abort(404, 'Pagamento não encontrado')