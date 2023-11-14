from flask import jsonify
from flask_jwt_extended import create_access_token
from ..models import Usuario

def requisitar_token(email):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        access_token = create_access_token(
            identity=usuario.id,
            )
        return {'access_token': access_token}    
    return {"mensagem": f"E-mail '{email}' não cadastrado"}, 401