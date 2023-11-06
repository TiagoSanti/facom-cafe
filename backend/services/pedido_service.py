from models import db, Pedido

def criar_pedido(id_usuario, data):
    pedido = Pedido(id_usuario=id_usuario, data=data, status='pendente')
    db.session.add(pedido)
    db.session.commit()
    return pedido

def listar_pedidos():
    return Pedido.query.all()

def localizar_pedido(id):
    return Pedido.query.filter_by(id=id).first()

def listar_pedidos_usuario(id_usuario):
    return Pedido.query.filter_by(id_usuario=id_usuario).all()

def excluir_pedido(id):
    pedido = Pedido.query.filter_by(id=id).first()
    db.session.delete(pedido)
    db.session.commit()
    return True

def atualizar_pedido(id, id_usuario, data, status):
    pedido = Pedido.query.filter_by(id=id).first()
    pedido.id_usuario = id_usuario
    pedido.data = data
    pedido.status = status
    db.session.commit()
    return pedido

def cancelar_pedido(id):
    pedido = Pedido.query.filter_by(id=id).first()
    pedido.status = 'cancelado'
    db.session.commit()
    return pedido

def concluir_pedido(id):
    pedido = Pedido.query.filter_by(id=id).first()
    pedido.status = 'concluido'
    db.session.commit()
    return pedido