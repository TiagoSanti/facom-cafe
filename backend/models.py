from sqlalchemy.schema import CheckConstraint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assinatura(db.Model):
    __tablename__ = 'assinatura'
    __table_args__ = (CheckConstraint("status IN ('ativa', 'cancelada', 'suspensa')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_plano = db.Column(db.Integer, db.ForeignKey('plano.id'), nullable=False)
    data_de_inicio = db.Column(db.Date, nullable=False)
    data_de_termino = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(9), nullable=False) # ativa, cancelada, suspensa

    # Relacionamentos
    usuario = db.relationship('Usuario', back_populates='assinaturas')
    plano = db.relationship('Plano', back_populates='assinaturas')
    pagamentos = db.relationship('Pagamento', back_populates='assinatura')

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_plano': self.id_plano,
            'data_de_inicio': self.data_de_inicio.isoformat(),
            'data_de_termino': self.data_de_termino.isoformat() if self.data_de_termino else None,
            'status': self.status,
        }
    
class ConfiguracoesNotificacao(db.Model):
    __tablename__ = 'configuracoesnotificacao'
    __table_args__ = (CheckConstraint("frequencia IN ('diário', 'semanal', 'mensal')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True)
    receber_email = db.Column(db.Boolean, nullable=False)
    receber_sms = db.Column(db.Boolean, nullable=False)
    frequencia = db.Column(db.String(7), nullable=False)
    
    # Relacionamentos
    usuario = db.relationship('Usuario', back_populates='configuracoes_notificacao', uselist=False)

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

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    tabela_modificada = db.Column(db.String(255), nullable=False)
    id_registro_modificado = db.Column(db.Integer, nullable=False)
    id_registro_modificado_secundario = db.Column(db.Integer, nullable=True)
    operacao = db.Column(db.String(50), nullable=False)
    data_hora_operacao = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tabela_modificada': self.tabela_modificada,
            'id_registro_modificado': self.id_registro_modificado,
            'id_registro_modificado_secundario': self.id_registro_modificado_secundario,
            'operacao': self.operacao,
            'data_hora_operacao': self.data_hora_operacao.isoformat(),
        }

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    __table_args__ = (CheckConstraint("metodo IN ('débito', 'crédito', 'pix')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_assinatura = db.Column(db.Integer, db.ForeignKey('assinatura.id'), nullable=False)
    valor = db.Column(db.Numeric, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    metodo = db.Column(db.String(7), nullable=False) # debito, credito, pix

    # Relacionamentos
    usuario = db.relationship('Usuario', back_populates='pagamentos')
    assinatura = db.relationship('Assinatura', back_populates='pagamentos')

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_assinatura': self.id_assinatura,
            'valor': float(self.valor),
            'data': self.data.isoformat(),
            'metodo': self.metodo,
        }

class Pedido(db.Model):
    __tablename__ = 'pedido'
    __table_args__ = (CheckConstraint("status IN ('concluído', 'cancelado', 'pendente')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False) # concluido, cancelado, pendente

    # Relacionamentos
    usuario = db.relationship('Usuario', back_populates='pedidos')
    pedido_produtos = db.relationship('PedidoProduto', back_populates='pedido')

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'data': self.data.isoformat(),
            'status': self.status,
        }
    
class PedidoProduto(db.Model):
    __tablename__ = 'pedidoproduto'

    # Atributos
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'), primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Numeric, nullable=False)

    # Relacionamentos
    pedido = db.relationship('Pedido', back_populates='pedido_produtos')
    produto = db.relationship('Produto', back_populates='pedido_produtos')

    def to_dict(self):
        return {
            'id_pedido': self.id_pedido,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade,
            'valor': float(self.valor),
        }

class Plano(db.Model):
    __tablename__ = 'plano'
    __table_args__ = (CheckConstraint("duracao IN ('1 mês', '3 meses', '6 meses', '12 meses')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric, nullable=False)
    duracao = db.Column(db.String(10), nullable=False)

    # Relacionamentos
    assinaturas = db.relationship('Assinatura', back_populates='plano')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': float(self.preco),
            'duracao': self.duracao,
        }

class Produto(db.Model):
    __tablename__ = 'produto'

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Numeric, nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    # Relacionamentos
    pedido_produtos = db.relationship('PedidoProduto', back_populates='produto')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': float(self.preco),
            'qtd_estoque': self.qtd_estoque,
            'descricao': self.descricao,
        }
  
class Usuario(db.Model):
    __tablename__ = 'usuario'

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefone = db.Column(db.String(15), unique=True, nullable=False)

    # Relacionamentos
    assinaturas = db.relationship('Assinatura', back_populates='usuario')
    pagamentos = db.relationship('Pagamento', back_populates='usuario')
    pedidos = db.relationship('Pedido', back_populates='usuario')
    configuracoes_notificacao = db.relationship('ConfiguracoesNotificacao', back_populates='usuario', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
        }
