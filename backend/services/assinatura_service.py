import re
from ..models import db, Assinatura, Plano, Usuario
from datetime import datetime

def criar_assinatura(id_usuario, id_plano, duracao):
    assinatura = Assinatura.query.filter_by(id_usuario=id_usuario, status='ativa').first()
    plano = Plano.query.filter_by(id=id_plano).first()
    usuario = Usuario.query.filter_by(id=id_usuario).first()

    if assinatura:
        return f'O usuário {usuario.email} já possui uma assinatura ativa'
    
    if not plano:
        return f'O id {id_plano} de plano não existe'
    
    if not usuario:
        return f'O id {id_usuario} de usuário não existe'
    
    if duracao not in ['mensal', 'trimestral', 'semestral', 'anual']:
        return f'O valor {duracao} de duração não existe'
    
    assinatura = Assinatura(id_usuario=id_usuario,
                            id_plano=id_plano,
                            duracao=duracao,
                            data_de_inicio=datetime.now(),
                            data_de_termino=None,
                            data_de_cancelamento=None,
                            data_de_suspensao=None,
                            status='ativa')
    
    db.session.add(assinatura)
    db.session.commit()
    return assinatura

def listar_assinaturas():
    return Assinatura.query.all()

def localizar_assinatura(id):
    return Assinatura.query.filter_by(id=id).first()

def excluir_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()

    if not assinatura:
        return f'O id {id} de assinatura não existe'
    
    db.session.delete(assinatura)
    db.session.commit()
    return assinatura

def atualizar_assinatura(id, id_usuario, id_plano, duracao):
    assinatura = Assinatura.query.filter_by(id=id).first()

    if not assinatura:
        return f'O id {id} de assinatura não existe'
    
    if Usuario.query.filter_by(id=id_usuario).first() is None:
        return f'O id {id_usuario} de usuário não existe'
    
    if Plano.query.filter_by(id=id_plano).first() is None:
        return f'O id {id_plano} de plano não existe'
    
    assinatura.id_usuario = id_usuario
    assinatura.id_plano = id_plano
    assinatura.duracao = duracao
    db.session.commit()
    return assinatura

def cancelar_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()

    if not assinatura:
        return f'O id {id} de assinatura não existe'
    
    if assinatura.status != 'ativa':
        return f'A assinatura {id} não está ativa para realizar o cancelamento'
    
    assinatura.status = 'cancelada'
    assinatura.data_de_cancelamento = datetime.now()

    db.session.commit()
    return assinatura

def suspender_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()

    if not assinatura:
        return f'O id {id} de assinatura não existe'
    
    if assinatura.status != 'ativa':
        return f'A assinatura {id} não está ativa para realizar a suspensão'
    
    assinatura.status = 'suspensa'
    assinatura.data_de_suspensao = datetime.now()

    db.session.commit()
    return assinatura

def reativar_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()

    if not assinatura:
        return f'O id {id} de assinatura não existe'
    
    if assinatura.status != 'inativa' and assinatura.status != 'suspensa':
        return f'A assinatura {id} não está inativa ou suspensa para realizar a reativação'
    
    assinatura.status = 'ativa'
    assinatura.data_de_suspensao = None
    db.session.commit()
    return assinatura