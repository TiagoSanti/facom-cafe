from functools import wraps
import os
from flask import request
import requests

TOKEN_SUB = os.getenv('TOKEN_SUB')

def validar_token_com_keycloak(token):
    url = 'https://auth.facoffee.hsborges.dev/realms/facoffee/protocol/openid-connect/userinfo'
    payload = ''

    if token.startswith('Bearer '):
        token = token.split(' ')[-1]

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request('POST', url, data=payload, headers=headers)
    
    if response.json().get('sub') != TOKEN_SUB:
        return False, 'Sub inválido'
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        return False, 'Token inválido ou expirado'

def requer_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {'mensagem': 'Token é necessário'}, 401

        token_valido, conteudo = validar_token_com_keycloak(token)
        
        if not token_valido:
            return {'mensagem': conteudo}, 401
        
        return f(*args, **kwargs)
    
    return decorated