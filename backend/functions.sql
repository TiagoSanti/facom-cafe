-- Função para capturar inserções, atualizações e exclusões e registrar na tabela Log
CREATE OR REPLACE FUNCTION registra_log() 
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT' OR TG_OP = 'UPDATE') THEN
        IF TG_TABLE_NAME = 'pedidoproduto' THEN
            INSERT INTO Log (tabela_modificada, id_registro_modificado, id_registro_modificado_secundario, operacao, data_hora_operacao)
            VALUES (TG_TABLE_NAME, NEW.id_pedido, NEW.id_produto, TG_OP, NOW());
        ELSE
            INSERT INTO Log (tabela_modificada, id_registro_modificado, operacao, data_hora_operacao)
            VALUES (TG_TABLE_NAME, NEW.id, TG_OP, NOW());
        END IF;
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        IF TG_TABLE_NAME = 'pedidoproduto' THEN
            INSERT INTO Log (tabela_modificada, id_registro_modificado, id_registro_modificado_secundario, operacao, data_hora_operacao)
            VALUES (TG_TABLE_NAME, OLD.id_pedido, OLD.id_produto, TG_OP, NOW());
        ELSE
            INSERT INTO Log (tabela_modificada, id_registro_modificado, operacao, data_hora_operacao)
            VALUES (TG_TABLE_NAME, OLD.id, TG_OP, NOW());
        END IF;
        RETURN OLD;
    END IF;
    EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error no registro de log da tabela %: %', TG_TABLE_NAME, SQLERRM;
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Criação da função que insere as configurações de notificação padrão
CREATE OR REPLACE FUNCTION adiciona_configuracoes_de_notificacao_padrao()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO ConfiguracoesNotificacao (id_usuario, receber_email, receber_sms, frequencia)
  VALUES (NEW.id, TRUE, TRUE, 'diário');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;