from symbol import parameters
from flask_restx import Namespace, Resource, reqparse, fields
from ..services.auth_service import *
from ..middleware import validar_token_com_keycloak
from flask import request

# Definindo o namespace
auth_ns = Namespace('auth', description='Operações relacionadas a autenticação')

token_generator_parser = reqparse.RequestParser()
token_generator_parser.add_argument('email', type=str, required=True, help='Email do usuário', location='json')

token_validation_parser = reqparse.RequestParser()
token_validation_parser.add_argument('token', type=str, required=True, help='Token de autenticação', location='json')

# Recurso para gerar token de autenticação
@auth_ns.route('/gerar-token')
class AuthGerarToken(Resource):
    @auth_ns.expect(token_generator_parser)
    @auth_ns.doc(
        description='Gera um token de autenticação para o usuário cadastrado na aplicação.',
        responses={
            200: 'Token gerado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o email não estiver cadastrado.'
        }
    )
    def post(self):
        args = token_generator_parser.parse_args()
        email = args['email']
        res = obter_token_keycloak(email)

        if isinstance(res, str):
            auth_ns.abort(400, res)
        else:
            return res, 200

# Recurso para validar token de autenticação
@auth_ns.route('/validar-token')
class AuthValidarToken(Resource):
    @auth_ns.expect(token_validation_parser)
    @auth_ns.doc(
        description='Valida um token de autenticação com o Keycloak.',
        responses={
            200: 'Token válido.',
            401: 'Token inválido ou expirado.'
        }
    )
    def post(self):
        args = token_validation_parser.parse_args()
        token = args['token']
        token_valido, user_info = validar_token_com_keycloak(token)
        
        if not token_valido:
            auth_ns.abort(401, 'Token inválido ou expirado.')
        else:
            return user_info, 200