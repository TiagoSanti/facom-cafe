-- Inserindo dados na tabela Usuario
INSERT INTO Usuario (nome, email, telefone) VALUES 
('João Silva', 'joao.silva@email.com', '1234-5678'),
('Maria Oliveira', 'maria.oliveira@email.com', '2345-6789'),
('Carlos Pereira', 'carlos.pereira@email.com', '3456-7890'),
('Ana Santos', 'ana.santos@email.com', '4567-8901'),
('Pedro Costa', 'pedro.costa@email.com', '5678-9012');

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

-- Inserindo dados na tabela Produto
INSERT INTO Produto (nome, preco, qtd_estoque, descricao) VALUES 
('Café Especial 250g', 25.00, 50, 'Café de origem única e processo de torra especial.'),
('Café Premium 500g', 45.00, 30, 'Café gourmet para paladares refinados.'),
('Café Tradicional 1kg', 30.00, 100, 'Para o dia a dia do amante de café.'),
('Cafeteira Elétrica', 120.00, 10, 'Prepare seu café com mais praticidade.'),
('Chá de Camomila 100g', 18.00, 50, 'Relaxe com nosso chá especial.');

-- Inserindo dados na tabela Pedido
INSERT INTO Pedido (id_usuario, data, status) VALUES 
(1, '2023-01-01 10:00:00', 'concluído'),
(2, '2023-01-15 14:00:00', 'pendente'),
(3, '2023-02-01 16:30:00', 'cancelado'),
(4, '2023-03-05 17:00:00', 'concluído'),
(5, '2023-04-10 18:30:00', 'pendente');

-- Inserindo dados na tabela PedidoProduto
INSERT INTO PedidoProduto (id_pedido, id_produto, quantidade, valor) VALUES 
(1, 1, 2, 50.00),
(1, 3, 1, 30.00),
(2, 2, 1, 45.00),
(3, 5, 3, 54.00),
(4, 4, 1, 120.00);