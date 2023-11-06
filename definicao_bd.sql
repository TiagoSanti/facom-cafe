DROP SCHEMA IF EXISTS facom_cafe_schema CASCADE;
CREATE SCHEMA facom_cafe_schema;
SET search_path TO facom_cafe_schema;

-- Criação da tabela Usuário
CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telefone VARCHAR(15) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Criação da tabela Plano
CREATE TABLE Plano (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco MONEY NOT NULL,
    duracao INTERVAL CHECK (
        duracao = INTERVAL '1 month' OR
        duracao = INTERVAL '3 months' OR
        duracao = INTERVAL '6 months' OR
        duracao = INTERVAL '1 year')
);

-- Criação da tabela Assinatura
CREATE TABLE Assinatura (
    id SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id),
    id_plano INT REFERENCES Plano(id),
    data_de_inicio DATE NOT NULL,
    data_de_termino DATE,
    status VARCHAR(9) NOT NULL CHECK (status IN ('ativa', 'cancelada', 'suspensa'))
);

-- Criação da tabela Pagamento
CREATE TABLE Pagamento (
    id SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id),
    id_assinatura INT REFERENCES Assinatura(id),
    valor MONEY NOT NULL,
    data TIMESTAMP NOT NULL,
    metodo VARCHAR(7) NOT NULL CHECK (metodo IN ('débito', 'crédito', 'pix'))
);

-- Criação da tabela Produto
CREATE TABLE Produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL NOT NULL,
    qtd_estoque INT NOT NULL,
    descricao TEXT
);

-- Criação da tabela Pedido
CREATE TABLE Pedido (
    id SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id),
    data TIMESTAMP NOT NULL,
    status VARCHAR(9) NOT NULL CHECK (status IN ('concluído', 'cancelado', 'pendente'))
);

-- Criação da tabela PedidoProduto
CREATE TABLE PedidoProduto (
    id_pedido INT REFERENCES Pedido(id),
    id_produto INT REFERENCES Produto(id),
    quantidade INT NOT NULL,
    valor MONEY NOT NULL,
    PRIMARY KEY (id_pedido, id_produto)
);

-- Criação da tabela ConfiguracoesNotificacao
CREATE TABLE ConfiguracoesNotificacao (
    id SERIAL PRIMARY KEY,
    id_usuario INT UNIQUE REFERENCES Usuario(id),
    receber_email BOOLEAN NOT NULL,
    receber_sms BOOLEAN NOT NULL,
    frequencia VARCHAR(7) NOT NULL CHECK (frequencia IN ('diário', 'semanal', 'mensal'))
);

-- Criação da tabela Log
CREATE TABLE Log (
    id SERIAL PRIMARY KEY,
    tabela_modificada VARCHAR(50) NOT NULL,
    id_registro_modificado INT NOT NULL,
    operacao VARCHAR(50) NOT NULL,
    data_hora_operacao TIMESTAMP NOT NULL
);

-- Função para capturar inserções, atualizações e exclusões e registrar na tabela Log
CREATE OR REPLACE FUNCTION register_log() 
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT' OR TG_OP = 'UPDATE') THEN
        INSERT INTO Log (tabela_modificada, id_registro_modificado, operacao, data_hora_operacao)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, NOW());
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO Log (tabela_modificada, id_registro_modificado, operacao, data_hora_operacao)
        VALUES (TG_TABLE_NAME, OLD.id, TG_OP, NOW());
        RETURN OLD;
    END IF;

    EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error in trigger: %', SQLERRM;
        IF (TG_OP = 'DELETE') THEN
            RETURN OLD;
        ELSE
            RETURN NEW;
        END IF;
END;
$$ LANGUAGE plpgsql;

-- Triggers para registrar alterações nas tabelas específicas

CREATE TRIGGER usuario_after_change
AFTER INSERT OR UPDATE OR DELETE ON Usuario
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER produto_after_change
AFTER INSERT OR UPDATE OR DELETE ON Produto
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER pedido_after_change
AFTER INSERT OR UPDATE OR DELETE ON Pedido
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER plano_after_change
AFTER INSERT OR UPDATE OR DELETE ON Plano
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER assinatura_after_change
AFTER INSERT OR UPDATE OR DELETE ON Assinatura
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER pagamento_after_change
AFTER INSERT OR UPDATE OR DELETE ON Pagamento
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER configuracoes_notificacao_after_change
AFTER INSERT OR UPDATE OR DELETE ON ConfiguracoesNotificacao
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER pedido_produto_after_change
AFTER INSERT OR UPDATE OR DELETE ON PedidoProduto
FOR EACH ROW EXECUTE FUNCTION register_log();

CREATE TRIGGER log_after_change
AFTER INSERT OR UPDATE OR DELETE ON Log
FOR EACH ROW EXECUTE FUNCTION register_log();