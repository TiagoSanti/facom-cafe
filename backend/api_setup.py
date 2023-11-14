from flask_restx import Api

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(
    authorizations=authorizations,
    security='Bearer Auth',
    version='1.0',
    title='Facom Café API',
    description='API para gerenciamento de assinaturas de café da Facom.'
)