from datetime import date, datetime
from .models import Usuario, Plano, Assinatura, Pagamento, Produto, Pedido
from .extensions import db

def create_and_populate_db():
    db.create_all()
'''

    usuarios = [
        Usuario(nome='João Silva', email='joao.silva@email.com', telefone='1234-5678', senha='senha123'),
        Usuario(nome='Maria Oliveira', email='maria.oliveira@email.com', telefone='2345-6789', senha='senha123'),
    ]

    db.session.bulk_save_objects(usuarios)

    planos = [
        Plano(nome='Plano Básico', descricao='-', preco=19.90, duracao='1 mês'),
        Plano(nome='Plano Intermediário', descricao='-', preco=49.90, duracao='3 meses'),
    ]

    db.session.bulk_save_objects(planos)

    assinaturas = [
        Assinatura(id_usuario=1, id_plano=1, data_de_inicio=date(2023, 1, 1), data_de_termino=date(2023, 2, 1), status='ativa'),
        Assinatura(id_usuario=2, id_plano=2, data_de_inicio=date(2023, 1, 15), data_de_termino=date(2023, 4, 15), status='ativa'),
    ]

    db.session.bulk_save_objects(assinaturas)

    pagamentos = [
        Pagamento(id_usuario=1, id_assinatura=1, valor=19.90, data=datetime(2023, 1, 1, 8, 0), metodo='crédito'),
        Pagamento(id_usuario=2, id_assinatura=2, valor=49.90, data=datetime(2023, 1, 15, 9, 30), metodo='pix'),
    ]

    db.session.bulk_save_objects(pagamentos)

    produtos = [        Produto(nome='Café Especial 250g', preco=25.00, qtd_estoque=50, descricao='Café de origem única e processo de torra especial.'),
        Produto(nome='Café Premium 500g', preco=45.00, qtd_estoque=30, descricao='Café gourmet para paladares refinados.'),
    ]

    db.session.bulk_save_objects(produtos)

    pedidos = [
        Pedido(id_usuario=1, data=datetime(2023, 1, 1, 10, 0), status='concluído'),
        Pedido(id_usuario=2, data=datetime(2023, 1, 15, 14, 0), status='pendente'),
    ]

    db.session.bulk_save_objects(pedidos)
    db.session.commit()
'''