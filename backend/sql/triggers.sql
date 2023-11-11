-- Triggers para registrar alterações nas tabelas específicas

CREATE OR REPLACE TRIGGER usuario_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Usuario
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER produto_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Produto
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER pedido_alterao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Pedido
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER plano_alteraao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Plano
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER assinatura_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Assinatura
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER pagamento_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON Pagamento
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER configuracoes_notificacao_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON ConfiguracoesNotificacao
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER pedido_produto_alteracao_trigger
AFTER INSERT OR UPDATE OR DELETE ON PedidoProduto
FOR EACH ROW EXECUTE FUNCTION registra_log();

CREATE OR REPLACE TRIGGER log_alteracao_trigger
AFTER UPDATE OR DELETE ON Log
FOR EACH ROW EXECUTE FUNCTION registra_log();


-- Criação do gatilho de configurações após inserção na tabela Usuario
CREATE OR REPLACE TRIGGER adiciona_configuracoes_de_notificacao_padrao_trigger
AFTER INSERT ON Usuario
FOR EACH ROW EXECUTE FUNCTION adiciona_configuracoes_de_notificacao_padrao();