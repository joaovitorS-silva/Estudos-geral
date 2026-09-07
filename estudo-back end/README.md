# Estudo Flask

Backend de estudos desenvolvido com Flask, SQLAlchemy, PostgreSQL e Alembic.

## O que existe atualmente

- Cadastro de usuários.
- Login com verificação de senha usando Argon2.
- Listagem de usuários.
- Busca de usuário por ID.
- Modelagem do usuário com nome, e-mail, senha, data de criação e administrador.
- Migrações do banco de dados com Alembic.
- Integração com um frontend separado em HTML e JavaScript.

## Frontend

O frontend fica em outro projeto, na pasta `Projetos/front-end(Flask)`. Ele não
fica dentro deste repositório do backend.

Atualmente, o frontend possui páginas simples para:

- Cadastro de usuário.
- Login.
- Listagem de usuários.

O frontend faz requisições para o backend em `http://127.0.0.1:5000`. Para
utilizá-lo, abra os arquivos HTML por um servidor local ou por uma extensão de
servidor estático do VS Code.

## Rotas atuais

| Método | Rota               | Descrição                      |
| ------ | ------------------ | ------------------------------ |
| `POST` | `/usuarios`        | Cria um usuário.               |
| `POST` | `/login`           | Verifica e-mail e senha.       |
| `GET`  | `/listar/usuarios` | Lista os usuários cadastrados. |
| `GET`  | `/procurar/<id>`   | Busca um usuário pelo ID.      |

## Tecnologias

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Argon2

## Configuração local

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Copie `.env.example` para `.env` e informe os dados do PostgreSQL:

   ```env
   DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/estudo_flask
   ALEMBIC_DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/estudo_flask
   ```

4. Execute as migrações:

   ```bash
   alembic upgrade head
   ```

5. Inicie a aplicação:

   ```bash
   python main.py
   ```

O backend será iniciado em `http://127.0.0.1:5000`.

## Próximas implementações

O próximo objetivo é implementar uma autenticação geral usando JWT.

- Gerar um token JWT após o login.
- Validar o token nas rotas protegidas.
- Criar um decorador para exigir autenticação.
- Definir permissões para usuários comuns e administradores.
- Impedir acesso à senha nas respostas da API.
- Adicionar expiração e renovação de tokens.
- Melhorar o tratamento de erros e validações.
- Adicionar testes automatizados para as rotas e autenticação.

## Segurança

- Nunca envie o arquivo `.env` para o GitHub.
- Nunca coloque senhas reais diretamente no código.
- As senhas dos usuários devem permanecer armazenadas apenas com hash.
- Em produção, utilize HTTPS e uma chave secreta segura para assinar os tokens JWT.
