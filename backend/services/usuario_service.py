from models import db, Usuario

def criar_usuario(nome, email, telefone, senha):
    usuario = Usuario(nome=nome, email=email, telefone=telefone, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return usuario

def listar_usuarios():
    return Usuario.query.all()

def localizar_usuario(id):
    return Usuario.query.filter_by(id=id).first()

def excluir_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
    return True

def atualizar_usuario(id, nome, email, telefone, senha):
    usuario = Usuario.query.filter_by(id=id).first()
    usuario.nome = nome
    usuario.email = email
    usuario.telefone = telefone
    usuario.senha = senha
    db.session.commit()
    return usuario