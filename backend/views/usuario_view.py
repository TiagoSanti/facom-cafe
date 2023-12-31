from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from ..services.usuario_service import *
from ..api_setup import api

# Definindo o namespace
usuario_ns = Namespace('usuarios', description='Operações relacionadas a usuários')

# Modelo para documentação da API
usuario_model = usuario_ns.model('Usuario', {
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'telefone': fields.String(required=True, description='Telefone do usuário')
})

# Recurso para criar usuário
@usuario_ns.route('/criar')
class UsuarioCriar(Resource):
    @jwt_required()
    @usuario_ns.doc(security='Bearer Auth')
    @usuario_ns.expect(usuario_model)
    @usuario_ns.response(201, 'Usuário criado com sucesso.')
    @usuario_ns.response(400, 'Erro de validação.')
    def post(self):
        body = usuario_ns.payload
        usuario = criar_usuario(**body)
        return usuario.to_dict(), 201

# Recurso para listar usuários
@usuario_ns.route('/listar')
class UsuarioListar(Resource):
    @usuario_ns.doc('listar_usuarios')
    @usuario_ns.response(200, 'Usuários listados com sucesso.')
    def get(self):
        usuarios = listar_usuarios()
        return [usuario.to_dict() for usuario in usuarios], 200

# Recurso para localizar usuário por ID
@usuario_ns.route('/localizar/<int:id>')
@usuario_ns.param('id', 'Identificador único do usuário')
class UsuarioLocalizar(Resource):
    @usuario_ns.doc('localizar_usuario')
    @usuario_ns.response(200, 'Usuário localizado com sucesso.')
    def get(self, id):
        usuario = localizar_usuario(id)
        return usuario.to_dict(), 200

# Recurso para excluir usuário
@usuario_ns.route('/excluir/<int:id>')
@usuario_ns.param('id', 'Identificador único do usuário')
class UsuarioExcluir(Resource):
    @usuario_ns.doc('excluir_usuario')
    @usuario_ns.response(200, 'Usuário excluído com sucesso.')
    def delete(self, id):
        excluir_usuario(id)
        return {'mensagem': 'Usuário excluído com sucesso'}, 200

# Recurso para atualizar usuário
@usuario_ns.route('/atualizar/<int:id>')
@usuario_ns.param('id', 'Identificador único do usuário')
class UsuarioAtualizar(Resource):
    @usuario_ns.expect(usuario_model)
    @usuario_ns.response(200, 'Usuário atualizado com sucesso.')
    def put(self, id):
        body = usuario_ns.payload
        usuario = atualizar_usuario(id, **body)
        return usuario.to_dict(), 200