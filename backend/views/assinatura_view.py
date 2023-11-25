from flask import request
from flask_restx import Namespace, Resource, fields
from ..services.assinatura_service import *
from ..models import Assinatura
from ..middleware import requer_token

# Definindo o namespace
assinatura_ns = Namespace('assinaturas', description='Operações relacionadas a assinaturas')

# Modelo para documentação da API
assinatura_create_model = assinatura_ns.model('AssinaturaCreate', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'id_plano': fields.Integer(required=True, description='ID do plano'),
    'duracao': fields.String(required=True, description='Duração da assinatura (mensal, trimestral, semestral, anual)')
})

assinatura_full_model = assinatura_ns.inherit('AssinaturaFull', assinatura_create_model, {
    'data_de_inicio': fields.Date(description='Data de início da assinatura'),
    'data_de_termino': fields.Date(description='Data de término da assinatura'),
    'data_de_cancelamento': fields.Date(description='Data de cancelamento da assinatura'),
    'data_de_suspensao': fields.Date(description='Data de suspensão da assinatura'),
    'status': fields.String(description='Status da assinatura (ativa, inativa, cancelada, suspensa)')
})

# Recurso para criar assinatura
@assinatura_ns.route('/')
class AssinaturaCriar(Resource):
    @assinatura_ns.expect(assinatura_create_model, validate=True)
    @assinatura_ns.doc('criar_assinatura',
        responses={
            201: 'Assinatura criada com sucesso.',
            400: 'Requisição inválida.'
        }
    )
    def post(self):
        dados = request.json
        res = criar_assinatura(**dados)

        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura criada com sucesso',
                    'assinatura': res.to_dict()}, 201
        else:
            assinatura_ns.abort(400, res)

    @requer_token
    @assinatura_ns.doc('listar_assinaturas',
        responses={
            200: 'Assinaturas listadas com sucesso.'
        }
    )
    def get(self):
        assinaturas = listar_assinaturas()
        return {'assinaturas': [assinatura.to_dict() for assinatura in assinaturas]}, 200

# Recurso para listar, localizar, atualizar e excluir assinaturas por ID
@assinatura_ns.route('/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaResource(Resource):
    @assinatura_ns.doc('localizar_assinatura',
        responses={
            200: 'Assinatura encontrada com sucesso.',
            404: 'Assinatura não encontrada.'
        }
    )
    def get(self, id):
        assinatura = localizar_assinatura(id)
        if assinatura:
            return {'assinatura': assinatura.to_dict()}, 200
        assinatura_ns.abort(404, 'Assinatura não encontrada')

    @assinatura_ns.expect(assinatura_full_model, validate=True)
    @assinatura_ns.doc('atualizar_assinatura',
        responses={
            200: 'Assinatura atualizada com sucesso.',
            400: 'Requisição inválida.',
            404: 'Assinatura não encontrada.'
        }
    )
    def put(self, id):
        dados = request.json
        res = atualizar_assinatura(id, **dados)

        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura atualizada com sucesso',
                    'assinatura': res.to_dict()}, 200
        else:
            assinatura_ns.abort(400, res)

    @assinatura_ns.doc('excluir_assinatura',
        responses={
            200: 'Assinatura excluída com sucesso.',
            404: 'Assinatura não encontrada.'
        }
    )
    def delete(self, id):
        res = excluir_assinatura(id)
        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura excluída com sucesso'}, 200
        assinatura_ns.abort(404, 'Assinatura não encontrada')

@assinatura_ns.route('/<int:id>/cancelar')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaCancelar(Resource):
    @assinatura_ns.doc('cancelar_assinatura',
        responses={
            200: 'Assinatura cancelada com sucesso.',
            400: 'Requisição inválida.'
        }
    )
    def post(self, id):
        res = cancelar_assinatura(id)
        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura cancelada com sucesso',
                    'assinatura': res.to_dict()}, 200
        assinatura_ns.abort(400, res)

@assinatura_ns.route('/<int:id>/suspender')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaSuspender(Resource):
    @assinatura_ns.doc('suspender_assinatura',
        responses={
            200: 'Assinatura suspensa com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se a assinatura não estiver ativa ou inativa'
        }
    )
    def post(self, id):
        res = suspender_assinatura(id)
        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura suspensa com sucesso',
                    'assinatura': res.to_dict()}, 200
        assinatura_ns.abort(400, res)

@assinatura_ns.route('/<int:id>/reativar')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaReativar(Resource):
    @assinatura_ns.doc('reativar_assinatura',
        responses={
            200: 'Assinatura reativada com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se a assinatura não estiver suspensa ou inativa'
        }
    )
    def post(self, id):
        res = reativar_assinatura(id)
        if isinstance(res, Assinatura):
            return {'mensagem': 'Assinatura reativada com sucesso',
                    'assinatura': res.to_dict()}, 200
        assinatura_ns.abort(400, res)
