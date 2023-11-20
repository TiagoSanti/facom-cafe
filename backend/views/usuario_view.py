from flask import request
from flask_restx import Namespace, Resource, fields
from ..services.usuario_service import *
from ..models import Usuario

# Definindo o namespace
usuario_ns = Namespace('usuarios', description='Operações relacionadas a usuários')

# Modelo para documentação da API
usuario_model = usuario_ns.model('Usuario', {
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'telefone': fields.String(required=True, description='Telefone do usuário')
})

# Recurso para criar e listar usuários
@usuario_ns.route('/')
class UsuarioCriarListar(Resource):
    @usuario_ns.expect(usuario_model, validate=True)
    @usuario_ns.doc(
        description='Cria um novo usuário com nome, email, e telefone.',
        responses={
            201: 'Usuário criado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o email já estiver em uso.'
        }
    )
    def post(self):
        dados = request.json
        res = criar_usuario(**dados)

        if isinstance(res, Usuario):
            return {'mensagem': 'Usuário criado com sucesso',
                    'usuario': res.to_dict()}, 201
        else:
            usuario_ns.abort(400, res)

    @usuario_ns.doc(
        description='Lista todos os usuários cadastrados.',
        responses={
            200: 'Usuários listados com sucesso.'
        }
    )
    def get(self):
        usuarios = listar_usuarios()
        return {'usuarios': [usuario.to_dict() for usuario in usuarios]}, 200

# Recurso para localizar, atualizar e excluir usuário por ID
@usuario_ns.route('/<int:id>')
@usuario_ns.param('id', 'Identificador único do usuário')
class UsuarioLocalizarAtualizarExcluir(Resource):
    @usuario_ns.doc(
        description='Localiza um usuário pelo ID.',
        params={
            'id': 'ID único representando o usuário.'
        },
        responses={
            200: 'Usuário encontrado com sucesso.',
            404: 'Usuário não encontrado.'
        }
    )
    def get(self, id):
        usuario = localizar_usuario(id)
        if usuario:
            return {'usuario': usuario.to_dict()}, 200
        usuario_ns.abort(404, 'Usuário não encontrado')

    @usuario_ns.expect(usuario_model, validate=True)
    @usuario_ns.doc(
        description='Atualiza um usuário pelo ID.',
        params={
            'id': 'ID único representando o usuário.'
        },
        responses={
            200: 'Usuário atualizado com sucesso.',
            400: 'Requisição inválida. Pode ocorrer se o email ou telefone já estiver em uso.',
            404: 'Usuário não encontrado.'
        }
    )
    def put(self, id):
        dados = request.json
        res = atualizar_usuario(id, **dados)

        if isinstance(res, Usuario):
            return {'mensagem': 'Usuário atualizado com sucesso',
                    'usuario': res.to_dict()}, 200
        elif isinstance(res, str) and 'válido' in res:
            usuario_ns.abort(404, res)
        else:
            usuario_ns.abort(400, res)

    @usuario_ns.doc(
        description='Exclui um usuário pelo ID.',
        params={
            'id': 'ID único representando o usuário.'
        },
        responses={
            200: 'Usuário excluído com sucesso.',
            404: 'Usuário não encontrado.'
        }
    )
    def delete(self, id):
        res = excluir_usuario(id)
        if isinstance(res, Usuario):
            return {'mensagem': 'Usuário excluído com sucesso',
                    'usuario': res.to_dict()}, 200
        usuario_ns.abort(404, 'Usuário não encontrado')