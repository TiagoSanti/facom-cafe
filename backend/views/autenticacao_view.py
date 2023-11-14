from flask_restx import Namespace, Resource, fields
from ..services.autenticacao_service import *
from flask_jwt_extended import jwt_required

# Definindo o namespace
autenticacao_ns = Namespace('autenticacao', description='Operações relacionadas a autenticação')

@autenticacao_ns.route('/requisitar_token')
class AutenticacaoRequisitarToken(Resource):
    @autenticacao_ns.doc('requisitar_token')
    @autenticacao_ns.response(200, 'Token requisitado com sucesso.')
    @autenticacao_ns.response(401, 'E-mail não cadastrado.')
    @autenticacao_ns.expect(autenticacao_ns.model('Autenticacao', {
        'email': fields.String(required=True, description='E-mail do usuário'),
    }))
    def post(self):
        body = autenticacao_ns.payload
        return requisitar_token(**body)