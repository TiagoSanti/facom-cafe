from ..models import Usuario, db, Pagamento, Assinatura, Plano, Usuario
from datetime import datetime

def criar_pagamento(id_usuario, id_assinatura, metodo):
    assinatura = Assinatura.query.filter_by(id=id_assinatura).first()

    if not assinatura:
        return f'O id {id_assinatura} de assinatura não existe'
    
    if Usuario.query.filter_by(id=id_usuario).first() is None:
        return f'O id {id_usuario} de usuário não existe'
    
    if metodo not in ['crédito', 'débito', 'pix']:
        return f'O método {metodo} não é válido'

    plano = Plano.query.filter_by(id=assinatura.id_plano).first()
    valor = plano.preco

    pagamento = Pagamento(id_usuario=id_usuario,
                          id_assinatura=id_assinatura,
                          valor=valor,
                          data=datetime.now(),
                          metodo=metodo)
    
    db.session.add(pagamento)
    db.session.commit()
    return pagamento

def listar_pagamentos():
    return Pagamento.query.all()

def localizar_pagamento(id):
    return Pagamento.query.filter_by(id=id).first()

def excluir_pagamento(id):
    pagamento = Pagamento.query.filter_by(id=id).first()

    if not pagamento:
        return f'O id {id} de pagamento não existe'

    db.session.delete(pagamento)
    db.session.commit()
    return pagamento

def atualizar_pagamento(id, id_usuario, id_assinatura, data, valor, metodo):
    pagamento = Pagamento.query.filter_by(id=id).first()

    print(pagamento.to_dict())

    if not pagamento:
        print(f'O id {id} de pagamento não existe')
        return f'O id {id} de pagamento não existe'
    
    if Usuario.query.filter_by(id=id_usuario).first() is None:
        print(f'O id {id_usuario} de usuário não existe')
        return f'O id {id_usuario} de usuário não existe'
    
    if Assinatura.query.filter_by(id=id_assinatura).first() is None:
        print(f'O id {id_assinatura} de assinatura não existe')
        return f'O id {id_assinatura} de assinatura não existe'
    
    if metodo not in ['crédito', 'débito', 'pix']:
        print(f'O método {metodo} não é válido')
        return f'O método {metodo} não é válido'

    pagamento.id_usuario = id_usuario
    pagamento.id_assinatura = id_assinatura
    pagamento.data = data
    pagamento.valor = valor
    pagamento.metodo = metodo
    db.session.commit()
    return pagamento