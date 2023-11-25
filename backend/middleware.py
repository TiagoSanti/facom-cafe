from functools import wraps
import os
from flask import request
import requests
from requests.exceptions import JSONDecodeError

AUTH_EMAIL = os.getenv('AUTH_EMAIL')

def validar_token_com_keycloak(token):
    url = 'https://auth.facoffee.hsborges.dev/realms/facoffee/protocol/openid-connect/userinfo'
    payload = ''

    if token.startswith('Bearer '):
        token = token.split(' ')[-1]

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request('POST', url, data=payload, headers=headers)

    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        return False, None

def requer_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {'mensagem': 'Token é necessário'}, 401

        token_valido, user_info = validar_token_com_keycloak(token)
        
        if not token_valido:
            return {'mensagem': 'Token inválido ou expirado.'}, 401
        
        if user_info['email'] != AUTH_EMAIL:
            return {'mensagem': 'Dados inválidos.'}, 401
        
        return f(*args, **kwargs)
    
    return decorated