from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from .models import db
from .views.assinatura_view import assinatura_ns
from .views.configuracoes_notificacao_view import configuracoes_notificacao_ns
from .views.log_view import log_ns
from .views.pagamento_view import pagamento_ns
from .views.pedido_view import pedido_ns
from .views.pedido_produto_view import pedido_produto_ns
from .views.plano_view import plano_ns
from .views.produto_view import produto_ns
from .views.usuario_view import usuario_ns

def create_app(DB_URI):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

    db.init_app(app)

    with app.app_context():
        db.create_all()

    CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}})

    api = Api(app,
            version='1.0',
            title='Facom Café API',
            description='API para gerenciamento de assinaturas de café da Facom.')

    api.add_namespace(assinatura_ns)
    api.add_namespace(configuracoes_notificacao_ns)
    api.add_namespace(log_ns)
    api.add_namespace(pagamento_ns)
    api.add_namespace(pedido_ns)
    api.add_namespace(pedido_produto_ns)
    api.add_namespace(plano_ns)
    api.add_namespace(produto_ns)
    api.add_namespace(usuario_ns)

    return app