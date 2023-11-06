from models import db, Plano

def criar_plano(nome, descricao, preco, duracao):
    plano = Plano(nome=nome, descricao=descricao, preco=preco, duracao=duracao)
    db.session.add(plano)
    db.session.commit()
    return plano

def listar_planos():
    return Plano.query.all()

def localizar_plano(id):
    return Plano.query.filter_by(id=id).first()

def excluir_plano(id):
    plano = Plano.query.filter_by(id=id).first()
    db.session.delete(plano)
    db.session.commit()
    return True

def atualizar_plano(id, nome, descricao, preco, duracao):
    plano = Plano.query.filter_by(id=id).first()
    plano.nome = nome
    plano.descricao = descricao
    plano.preco = preco
    plano.duracao = duracao
    db.session.commit()
    return plano