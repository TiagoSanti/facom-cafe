from ..models import db, Pagamento

def criar_pagamento(id_usuario, id_plano, data, valor):
    pagamento = Pagamento(id_usuario=id_usuario, id_plano=id_plano, data=data, valor=valor)
    db.session.add(pagamento)
    db.session.commit()
    return pagamento

def listar_pagamentos():
    return Pagamento.query.all()

def localizar_pagamento(id):
    return Pagamento.query.filter_by(id=id).first()

def excluir_pagamento(id):
    pagamento = Pagamento.query.filter_by(id=id).first()
    db.session.delete(pagamento)
    db.session.commit()
    return True

def atualizar_pagamento(id, id_usuario, id_plano, data, valor):
    pagamento = Pagamento.query.filter_by(id=id).first()
    pagamento.id_usuario = id_usuario
    pagamento.id_plano = id_plano
    pagamento.data = data
    pagamento.valor = valor
    db.session.commit()
    return pagamento

def listar_pagamentos_por_usuario(id_usuario):
    return Pagamento.query.filter_by(id_usuario=id_usuario).all()

def listar_pagamentos_por_periodo(data_inicio, data_fim):
    return Pagamento.query.filter(Pagamento.data.between(data_inicio, data_fim)).all()

def listar_pagamentos_por_periodo_usuario(id_usuario, data_inicio, data_fim):
    return Pagamento.query.filter(Pagamento.id_usuario==id_usuario, Pagamento.data.between(data_inicio, data_fim)).all()