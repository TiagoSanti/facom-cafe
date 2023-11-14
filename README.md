# [Facom Café](https://github.com/TiagoSanti/facom-cafe)

## Trabalho LBD

**Grupo 4**

Lourdes Oshiro Igarashi - 2021.1906.032-8

Ryan Breda Santos - 2021.1906.005-0

Tiago Clarintino Santi - 2021.1906.036-0

## Trabalho TADS

Lourdes Oshiro Igarashi - 2021.1906.032-8

Tiago Clarintino Santi - 2021.1906.036-0

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
DATABASE_URI=postgresql://user_name:password@host:port/database_name
```

Ao executar os passos anteriores, a API estará disponível em <http://localhost:5000/>.
