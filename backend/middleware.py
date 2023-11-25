from functools import wraps
from flask import request, jsonify
import requests

def validar_token_com_keycloak(token):
    url = 'https://auth.facoffee.hsborges.dev/realms/facoffee/protocol/openid-connect/userinfo'

    payload = ''
    headers = {
        'User-Agent': 'insomnia/8.3.0',
        'Authorization': f'Bearer {token}'
    }

    response = requests.request('POST', url, data=payload, headers=headers)

    if response.status_code == 200:
        return True, response.json()
    else:
        return False, None

def requer_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {"mensagem": "Token é necessário"}, 401

        token_valido, user_info = validar_token_com_keycloak(token)
        
        if not token_valido:
            return jsonify({'mensagem': 'Token inválido ou expirado.'}), 401
        
        return f(*args, **kwargs)
    
    return decorated