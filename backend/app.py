from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from .models import db
from .api_setup import api

from .views.assinatura_view import assinatura_ns
from .views.autenticacao_view import autenticacao_ns
from .views.configuracoes_notificacao_view import configuracoes_notificacao_ns
from .views.log_view import log_ns
from .views.pagamento_view import pagamento_ns
from .views.pedido_view import pedido_ns
from .views.pedido_produto_view import pedido_produto_ns
from .views.plano_view import plano_ns
from .views.produto_view import produto_ns
from .views.usuario_view import usuario_ns

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    jwt = JWTManager(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}})

    api.init_app(app)

    api.add_namespace(assinatura_ns)
    api.add_namespace(autenticacao_ns)
    api.add_namespace(configuracoes_notificacao_ns)
    api.add_namespace(log_ns)
    api.add_namespace(pagamento_ns)
    api.add_namespace(pedido_ns)
    api.add_namespace(pedido_produto_ns)
    api.add_namespace(plano_ns)
    api.add_namespace(produto_ns)
    api.add_namespace(usuario_ns)

    return app