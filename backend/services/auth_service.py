import requests
from .usuario_service import localizar_usuario_por_email
import os

AUTH_EMAIL = os.getenv('AUTH_EMAIL')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')

def obter_token_keycloak(email):
    
    if localizar_usuario_por_email(email) is None:
        return 'Usuário não existe'

    url = 'https://auth.facoffee.hsborges.dev/realms/facoffee/protocol/openid-connect/token'
    data = {
        'client_id': 'facoffee',
        'grant_type': 'password',
        'username': AUTH_EMAIL,
        'password': AUTH_PASSWORD,
        'scope': 'openid'
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        return {'token': response.json()['access_token']}
    else:
        return 'Erro ao obter token do keycloak'