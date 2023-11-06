from models import db, Produto

def criar_produto(nome, preco, qtd_estoque, descricao):
    produto = Produto(nome=nome, preco=preco, qtd_estoque=qtd_estoque, descricao=descricao)
    db.session.add(produto)
    db.session.commit()
    return produto

def listar_produtos():
    return Produto.query.all()

def localizar_produto(id):
    return Produto.query.filter_by(id=id).first()

def excluir_produto(id):
    produto = Produto.query.filter_by(id=id).first()
    db.session.delete(produto)
    db.session.commit()
    return True

def atualizar_produto(id, nome, preco, qtd_estoque, descricao):
    produto = Produto.query.filter_by(id=id).first()
    produto.nome = nome
    produto.preco = preco
    produto.qtd_estoque = qtd_estoque
    produto.descricao = descricao
    db.session.commit()
    return produto

def adicionar_estoque(id, qtd):
    produto = Produto.query.filter_by(id=id).first()
    produto.qtd_estoque += qtd
    db.session.commit()
    return produto

def remover_estoque(id, qtd):
    produto = Produto.query.filter_by(id=id).first()
    produto.qtd_estoque -= qtd
    db.session.commit()
    return produto
