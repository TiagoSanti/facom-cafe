from ..models import db, Plano

def criar_plano(nome, descricao, preco):
    plano = localizar_plano_por_nome(nome)

    if plano:
        return f'O nome {nome} já está cadastrado'
            
    plano = Plano(nome=nome,
                  descricao=descricao,
                  preco=preco)
    
    db.session.add(plano)
    db.session.commit()
    return plano

def listar_planos():
    return Plano.query.all()

def localizar_plano(id):
    return Plano.query.filter_by(id=id).first()

def localizar_plano_por_nome(nome):
    return Plano.query.filter_by(nome=nome).first()

def excluir_plano(id):
    plano = Plano.query.filter_by(id=id).first()

    if not plano:
        return f'O id {id} de plano não existe'

    db.session.delete(plano)
    db.session.commit()
    return plano

def atualizar_plano(id, nome, descricao, preco):
    plano = Plano.query.filter_by(id=id).first()

    if not plano:
        return f'O id {id} de plano não existe'
    
    if plano.nome != nome and Plano.query.filter_by(nome=nome).first() is not None:
        return f'O nome {nome} já está cadastrado'

    plano.nome = nome
    plano.descricao = descricao
    plano.preco = preco
    db.session.commit()
    return plano