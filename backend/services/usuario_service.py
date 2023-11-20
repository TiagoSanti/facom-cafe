from ..models import db, Usuario

def criar_usuario(nome, email, telefone):
    usuario = localizar_usuario_por_email(email)

    if usuario:
        return f'O email {email} já está cadastrado'
    
    if Usuario.query.filter_by(telefone=telefone).first() is not None:
        return f'O telefone {telefone} já está cadastrado'
    
    usuario = Usuario(nome=nome,
                      email=email,
                      telefone=telefone)
    
    db.session.add(usuario)
    db.session.commit()
    return usuario

def listar_usuarios():
    return Usuario.query.all()

def localizar_usuario(id):
    return Usuario.query.filter_by(id=id).first()

def localizar_usuario_por_email(email):
    return Usuario.query.filter_by(email=email).first()

def excluir_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()

    if not usuario:
        return f'O id {id} de usuário não existe'

    db.session.delete(usuario)
    db.session.commit()
    return usuario

def atualizar_usuario(id, nome, email, telefone):
    usuario = Usuario.query.filter_by(id=id).first()

    if not usuario:
        return f'O id {id} de usuário não existe'

    if usuario.email != email and Usuario.query.filter_by(email=email).first() is not None:
        return f'O email {email} já está cadastrado'
    
    if usuario.telefone != telefone and Usuario.query.filter_by(telefone=telefone).first() is not None:
        return f'O telefone {telefone} já está cadastrado'

    usuario.nome = nome
    usuario.email = email
    usuario.telefone = telefone
    db.session.commit()
    return usuario