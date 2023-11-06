from flask_restx import Namespace, Resource, fields
from services.assinatura_service import *

# Definindo o namespace
assinatura_ns = Namespace('assinaturas', description='Operações relacionadas a assinaturas')

# Modelo para documentação da API
assinatura_model = assinatura_ns.model('Assinatura', {
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'id_plano': fields.Integer(required=True, description='ID do plano'),
    'data_inicio': fields.Date(required=True, description='Data de início da assinatura'),
    'data_fim': fields.Date(required=True, description='Data de fim da assinatura'),
    'status': fields.String(required=True, description='Status da assinatura (ativa, cancelada, suspensa)')
})

# Recurso para criar assinatura
@assinatura_ns.route('/criar')
class AssinaturaCriar(Resource):
    @assinatura_ns.expect(assinatura_model)
    @assinatura_ns.response(201, 'Assinatura criada com sucesso.')
    def post(self):
        body = assinatura_ns.payload
        assinatura = criar_assinatura(**body)
        return assinatura.to_dict(), 201

# Recurso para listar assinaturas
@assinatura_ns.route('/listar')
class AssinaturaListar(Resource):
    @assinatura_ns.doc('listar_assinaturas')
    def get(self):
        assinaturas = listar_assinaturas()
        return [assinatura.to_dict() for assinatura in assinaturas], 200

# Recurso para localizar assinatura por ID
@assinatura_ns.route('/localizar/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaLocalizar(Resource):
    @assinatura_ns.doc('localizar_assinatura')
    def get(self, id):
        assinatura = localizar_assinatura(id)
        return assinatura.to_dict(), 200

# Recurso para excluir assinatura
@assinatura_ns.route('/excluir/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaExcluir(Resource):
    @assinatura_ns.doc('excluir_assinatura')
    def delete(self, id):
        excluir_assinatura(id)
        return {'mensagem': 'Assinatura excluída com sucesso'}, 200

# Recurso para atualizar assinatura
@assinatura_ns.route('/atualizar/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaAtualizar(Resource):
    @assinatura_ns.expect(assinatura_model)
    @assinatura_ns.doc('atualizar_assinatura')
    def put(self, id):
        body = assinatura_ns.payload
        assinatura = atualizar_assinatura(id, **body)
        return assinatura.to_dict(), 200

# Recurso para cancelar assinatura
@assinatura_ns.route('/cancelar/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
@assinatura_ns.param('data_fim', 'Data de fim da assinatura')
class AssinaturaCancelar(Resource):
    @assinatura_ns.doc('cancelar_assinatura')
    def post(self, id, data_fim):
        assinatura = cancelar_assinatura(id, data_fim)
        return assinatura.to_dict(), 200

# Recurso para suspender assinatura
@assinatura_ns.route('/suspender/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaSuspender(Resource):
    @assinatura_ns.doc('suspender_assinatura')
    def post(self, id):
        assinatura = suspender_assinatura(id)
        return assinatura.to_dict(), 200

# Recurso para reativar assinatura
@assinatura_ns.route('/reativar/<int:id>')
@assinatura_ns.param('id', 'Identificador único da assinatura')
class AssinaturaReativar(Resource):
    @assinatura_ns.doc('reativar_assinatura')
    def post(self, id):
        assinatura = reativar_assinatura(id)
        return assinatura.to_dict(), 200