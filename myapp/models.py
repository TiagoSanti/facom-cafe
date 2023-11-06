from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefone = db.Column(db.String(15), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
        }

class Plano(db.Model):
    __tablename__ = 'plano'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric, nullable=False)
    duracao = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'duracao': self.duracao,
        }

class Assinatura(db.Model):
    __tablename__ = 'assinatura'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_plano = db.Column(db.Integer, db.ForeignKey('plano.id'), nullable=False)
    data_de_inicio = db.Column(db.Date, nullable=False)
    data_de_termino = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(9), nullable=False) # ativa, cancelada, suspensa

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_plano': self.id_plano,
            'data_de_inicio': self.data_de_inicio,
            'data_de_termino': self.data_de_termino,
            'status': self.status,
        }

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_assinatura = db.Column(db.Integer, db.ForeignKey('assinatura.id'), nullable=False)
    valor = db.Column(db.Numeric, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    metodo = db.Column(db.String(7), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_assinatura': self.id_assinatura,
            'valor': self.valor,
            'data': self.data,
            'metodo': self.metodo,
        }
    
class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False) # concluido, cancelado, pendente

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'data': self.data,
            'status': self.status,
        }

class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Numeric, nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'qtd_estoque': self.qtd_estoque,
            'descricao': self.descricao,
        }

class PedidoProduto(db.Model):
    __tablename__ = 'pedidoproduto'
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'), primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Numeric, nullable=False)

    def to_dict(self):
        return {
            'id_pedido': self.id_pedido,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade,
            'valor': self.valor,
        }

class ConfiguracoesNotificacao(db.Model):
    __tablename__ = 'configuracoesnotificacao'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)
    receber_email = db.Column(db.Boolean, nullable=False)
    receber_sms = db.Column(db.Boolean, nullable=False)
    frequencia = db.Column(db.String(7), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'receber_email': self.receber_email,
            'receber_sms': self.receber_sms,
            'frequencia': self.frequencia,
        }

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    tabela_modificada = db.Column(db.String(255), nullable=False)
    id_registro_modificado = db.Column(db.Integer, nullable=False)
    operacao = db.Column(db.String(50), nullable=False)
    data_hora_operacao = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tabela_modificada': self.tabela_modificada,
            'id_registro_modificado': self.id_registro_modificado,
            'operacao': self.operacao,
            'data_hora_operacao': self.data_hora_operacao,
        }