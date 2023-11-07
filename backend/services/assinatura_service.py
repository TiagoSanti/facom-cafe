from ..models import db, Assinatura

def criar_assinatura(id_usuario, id_plano, data_inicio, data_fim):
    assinatura = Assinatura(id_usuario=id_usuario, id_plano=id_plano, data_inicio=data_inicio, data_fim=data_fim, status='ativa')
    db.session.add(assinatura)
    db.session.commit()
    return assinatura

def listar_assinaturas():
    return Assinatura.query.all()

def localizar_assinatura(id):
    return Assinatura.query.filter_by(id=id).first()

def excluir_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()
    db.session.delete(assinatura)
    db.session.commit()
    return True

def atualizar_assinatura(id, id_usuario, id_plano, data_inicio, data_fim, status):
    assinatura = Assinatura.query.filter_by(id=id).first()
    assinatura.id_usuario = id_usuario
    assinatura.id_plano = id_plano
    assinatura.data_inicio = data_inicio
    assinatura.data_fim = data_fim
    assinatura.status = status
    db.session.commit()
    return assinatura

def cancelar_assinatura(id, data_fim):
    assinatura = Assinatura.query.filter_by(id=id).first()
    assinatura.data_fim = data_fim
    assinatura.status = 'cancelada'
    db.session.commit()
    return assinatura

def suspender_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()
    assinatura.status = 'suspensa'
    db.session.commit()
    return assinatura

def reativar_assinatura(id):
    assinatura = Assinatura.query.filter_by(id=id).first()
    assinatura.status = 'ativa'
    db.session.commit()
    return assinatura