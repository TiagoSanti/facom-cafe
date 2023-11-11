from ..models import Log

def listar_logs():
    return Log.query.all()

def localizar_log(id):
    return Log.query.filter_by(id=id).first()

def listar_logs_por_tabela(tabela):
    return Log.query.filter_by(tabela_modificada=tabela).all()

def listar_logs_por_modificacao(modificacao):
    return Log.query.filter_by(modificacao=modificacao).all()

def listar_logs_por_intervalo_data(data_inicio, data_fim):
    return Log.query.filter(Log.data.between(data_inicio, data_fim)).all()