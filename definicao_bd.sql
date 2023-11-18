-- Inserindo dados na tabela Usuario
INSERT INTO Usuario (nome, email, telefone, senha) VALUES 
('João Silva', 'joao.silva@email.com', '1234-5678', 'senha123'),
('Maria Oliveira', 'maria.oliveira@email.com', '2345-6789', 'senha123'),
('Carlos Pereira', 'carlos.pereira@email.com', '3456-7890', 'senha123'),
('Ana Santos', 'ana.santos@email.com', '4567-8901', 'senha123'),
('Pedro Costa', 'pedro.costa@email.com', '5678-9012', 'senha123');

-- Inserindo dados na tabela Plano
INSERT INTO Plano (nome, descricao, preco, duracao) VALUES 
('Plano Básico', '-', 19.90, '1 mês'),
('Plano Intermediário', '-', 49.90, '3 meses'),
('Plano Avançado', '-', 99.90, '6 meses'),
('Plano Profissional', '-', 199.90, '12 meses'),
('Plano Ultimate', '-', 299.90, '12 meses');

-- Inserindo dados na tabela Assinatura
INSERT INTO Assinatura (id_usuario, id_plano, data_de_inicio, data_de_termino, status) VALUES 
(1, 1, '2023-01-01', '2023-02-01', 'ativa'),
(2, 2, '2023-01-15', '2023-04-15', 'ativa'),
(3, 3, '2023-02-01', '2023-08-01', 'ativa'),
(4, 4, '2023-03-01', NULL, 'suspensa'),
(5, 5, '2023-04-01', NULL, 'cancelada');

-- Inserindo dados na tabela Pagamento
INSERT INTO Pagamento (id_usuario, id_assinatura, valor, data, metodo) VALUES 
(1, 1, 19.90, '2023-01-01 08:00:00', 'crédito'),
(2, 2, 49.90, '2023-01-15 09:30:00', 'pix'),
(3, 3, 99.90, '2023-02-01 10:45:00', 'débito'),
(4, 4, 199.90, '2023-03-01 11:00:00', 'crédito'),
(5, 5, 299.90, '2023-04-01 12:00:00', 'pix');