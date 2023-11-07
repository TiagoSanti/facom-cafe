# Facom Café

## Execução do Backend

1. Instalar o Python 3.9.13

2. Abrir o terminal na pasta do projeto e no diretório backend

    ```bash
    cd backend
    ```

3. Criar um ambiente virtual

    ```bash
    python -m venv venv
    ```

4. Ativar o ambiente virtual

   - Para windows:

   ```bash
   venv\Scripts\activate.bat
   ```

   - Para linux:

   ```bash
   venv\Scripts\activate
   ```

5. Instalar as dependências

    ```bash
    pip install -r requirements.txt
    ```

6. Voltar para a pasta raiz do projeto

    ```bash
    cd ..
    ```

7. Executar o backend

    ```bash
    python -m backend.run
    ```

Para que o backend faça a conexão com o banco de dados, é necessário criar um arquivo .env na pasta backend com a variável de ambiente que contém a string de conexão com o banco de dados.

```bash
# backend/.env Exemplo de string de conexão com o banco de dados postgresql
DATABASE_URI=postgresql://postgres:postgres@localhost/database_name
```

O nome da variável é de sua escolha, mas esse nome deve ser colocado no argumento da função os.getenv() no arquivo backend/run.py:

```python
# backend/run.py
app = create_app(os.getenv('DATABASE_URI'))
```

Ao executar os passos anteriores, a API estará disponível em <http://localhost:5000/>.
