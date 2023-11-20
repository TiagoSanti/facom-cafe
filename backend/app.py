from flask import Flask
from flask_cors import CORS
import os
from .models import db
from .api_setup import api

from .views.assinatura_view import assinatura_ns
from .views.pagamento_view import pagamento_ns
from .views.plano_view import plano_ns
from .views.usuario_view import usuario_ns

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}})

    api.init_app(app)

    api.add_namespace(assinatura_ns)
    api.add_namespace(pagamento_ns)
    api.add_namespace(plano_ns)
    api.add_namespace(usuario_ns)

    return app