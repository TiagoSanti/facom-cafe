from models import db, ConfiguracoesNotificacao

def criar_configuracoes_notificacao(id_usuario, receber_email=True, receber_sms=True, frequencia='diário'):
    configuracoes_notificacao = ConfiguracoesNotificacao(id_usuario=id_usuario, receber_email=receber_email, receber_sms=receber_sms, frequencia=frequencia)
    db.session.add(configuracoes_notificacao)
    db.session.commit()
    return configuracoes_notificacao

def listar_configuracoes_notificacoes():
    return ConfiguracoesNotificacao.query.all()

def localizar_configuracoes_notificacao(id):
    return ConfiguracoesNotificacao.query.filter_by(id=id).first()

def localizar_configuracoes_notificacao_por_usuario(id_usuario):
    return ConfiguracoesNotificacao.query.filter_by(id_usuario=id_usuario).first()

def excluir_configuracoes_notificacao(id):
    configuracoes_notificacao = ConfiguracoesNotificacao.query.filter_by(id=id).first()
    db.session.delete(configuracoes_notificacao)
    db.session.commit()
    return True

def atualizar_configuracoes_notificacao(id, receber_email, receber_sms, frequencia):
    configuracoes_notificacao = ConfiguracoesNotificacao.query.filter_by(id=id).first()
    configuracoes_notificacao.receber_email = receber_email
    configuracoes_notificacao.receber_sms = receber_sms
    configuracoes_notificacao.frequencia = frequencia
    db.session.commit()
    return configuracoes_notificacao

def atualizar_configuracoes_notificacao_por_usuario(id_usuario, receber_email, receber_sms, frequencia):
    configuracoes_notificacao = ConfiguracoesNotificacao.query.filter_by(id_usuario=id_usuario).first()
    configuracoes_notificacao.receber_email = receber_email
    configuracoes_notificacao.receber_sms = receber_sms
    configuracoes_notificacao.frequencia = frequencia
    db.session.commit()
    return configuracoes_notificacao
