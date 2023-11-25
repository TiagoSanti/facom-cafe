from flask_restx import Namespace, Resource, reqparse, fields
from ..services.auth_service import *
from ..middleware import validar_token_com_keycloak
from flask import request

# Definindo o namespace
auth_ns = Namespace('auth', description='Operações relacionadas a autenticação')

generator_parser = reqparse.RequestParser()
generator_parser.add_argument('email', type=str, required=True, help='Email do usuário', location='json')

validation_parser = reqparse.RequestParser()
validation_parser.add_argument('token', type=str, required=True, help='Token de autenticação', location='json')

@auth_ns.route('/gerar-token')
class AuthGerarToken(Resource):
    @auth_ns.expect(generator_parser)
    @auth_ns.doc(
        description='Gera um token de autenticação para o usuário.',
        responses={
            200: 'Token gerado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o email não estiver cadastrado.'
        }
    )
    def post(self):
        args = generator_parser.parse_args()
        email = args['email']
        res = obter_token_keycloak(email)

        if isinstance(res, str):
            auth_ns.abort(400, res)
        else:
            return res, 200
        
@auth_ns.route('/validar-token')
class AuthValidarToken(Resource):
    @auth_ns.expect(validation_parser)
    @auth_ns.doc(
        description='Valida um token de autenticação.',
        responses={
            200: 'Token válido.',
            401: 'Token inválido ou expirado.'
        }
    )
    def post(self):
        args = validation_parser.parse_args()
        token = args['token']
        token_valido, user_info = validar_token_com_keycloak(token)
        
        if not token_valido:
            auth_ns.abort(401, 'Token inválido ou expirado.')
        else:
            return user_info, 200