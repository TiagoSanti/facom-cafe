from ..models import db, PedidoProduto

def criar_pedido_produto(id_pedido, id_produto, quantidade, valor):
    pedido_produto = PedidoProduto(id_pedido=id_pedido, id_produto=id_produto, quantidade=quantidade, valor=valor)
    db.session.add(pedido_produto)
    db.session.commit()
    return pedido_produto

def listar_pedidos_produtos():
    return PedidoProduto.query.all()

def localizar_pedido_produto(id_pedido, id_produto):
    return PedidoProduto.query.filter_by(id_pedido=id_pedido, id_produto=id_produto).first()

def excluir_pedido_produto(id_pedido, id_produto):
    pedido_produto = PedidoProduto.query.filter_by(id_pedido=id_pedido, id_produto=id_produto).first()
    db.session.delete(pedido_produto)
    db.session.commit()
    return True

def atualizar_pedido_produto(id_pedido, id_produto, quantidade, valor):
    pedido_produto = PedidoProduto.query.filter_by(id_pedido=id_pedido, id_produto=id_produto).first()
    pedido_produto.quantidade = quantidade
    pedido_produto.valor = valor
    db.session.commit()
    return pedido_produto