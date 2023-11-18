from .extensions import db

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
    duracao = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': float(self.preco),
            'duracao': self.duracao,
        }

class Assinatura(db.Model):
    __tablename__ = 'assinatura'
    __table_args__ = (CheckConstraint("status IN ('ativa', 'cancelada', 'suspensa')"), {})
    __table_args__ = (CheckConstraint("duracao IN ('1 mês', '3 meses', '6 meses', '12 meses')"), {})

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_plano = db.Column(db.Integer, db.ForeignKey('plano.id'), nullable=False)
    duracao = db.Column(db.String(10), nullable=False)
    data_de_inicio = db.Column(db.Date, nullable=False)
    data_de_termino = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(9), nullable=False) # ativa, cancelada, suspensa

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_plano': self.id_plano,
            'data_de_inicio': self.data_de_inicio.isoformat(),
            'data_de_termino': self.data_de_termino.isoformat() if self.data_de_termino else None,
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
            'valor': float(self.valor),
            'data': self.data.isoformat(),
            'metodo': self.metodo,
        }
    
class Plano(db.Model):
    __tablename__ = 'plano'

    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric, nullable=False)

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

    def to_dict(self):
        return {
            'id': self.id,
            'tabela_modificada': self.tabela_modificada,
            'id_registro_modificado': self.id_registro_modificado,
            'operacao': self.operacao,
            'data_hora_operacao': self.data_hora_operacao.isoformat(),
        }