from flask_restx import Api

authorizations = {
    'Bearer Token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Digite \'Bearer <<token>>\' no campo abaixo.'
    },
}

api = Api(
    version='1.0',
    title='Facom Café API',
    description='API para gerenciamento de assinaturas de café da Facom.',
    authorizations=authorizations,
    security='Bearer Token'
)