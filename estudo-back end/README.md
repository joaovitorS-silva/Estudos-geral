# Estudo Flask — API de usuários

Backend desenvolvido para estudar a construção de uma API com Flask, autenticação JWT, autorização por funções e persistência em PostgreSQL.

O projeto prioriza o aprendizado dos fundamentos, mantendo uma estrutura simples e sem camadas desnecessárias.

## Funcionalidades atuais

- Cadastro de usuários com validação por Pydantic.
- Validação de nome, e-mail e tamanho da senha.
- Senhas armazenadas com hash Argon2.
- Login com access token e refresh token JWT.
- Tokens enviados em cookies `HttpOnly`.
- Renovação do access token por meio do refresh token.
- Logout com remoção dos cookies.
- Proteção de rotas com um decorador de autenticação.
- Controle de acesso pelas funções `user` e `admin`.
- Listagem e busca de usuários disponíveis apenas para administradores.
- Migrações do banco de dados com Alembic.
- Integração com o frontend simples presente neste repositório.

## Tecnologias

- Python
- Flask
- Flask-CORS
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Argon2
- PyJWT
- python-dotenv

## Estrutura do backend

```text
estudo-back end/
├── alembic/
│   └── versions/
├── routes/
│   ├── auth.py
│   └── users.py
├── .env.example
├── alembic.ini
├── dependencias.py
├── main.py
├── models.py
├── requirements.txt
├── Schemas.py
└── README.md
```

## Configuração local

### 1. Entre na pasta do backend

```bash
cd "estudo-back end"
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Preencha o `.env` com os dados do PostgreSQL e uma chave JWT:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/estudo_flask
ALEMBIC_DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/estudo_flask
JWT_SECRET=sua_chave_secreta
ALGORITHM=HS256
```

Uma chave pode ser gerada localmente com:

```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

Nunca envie o arquivo `.env` para o GitHub.

### 5. Execute as migrações

```bash
alembic upgrade head
```

Para verificar o estado das migrações:

```bash
alembic current
alembic check
```

### 6. Inicie a aplicação

```bash
python main.py
```

A API será iniciada em `http://127.0.0.1:5000`.

## Rotas atuais

| Método | Rota | Acesso | Descrição |
| --- | --- | --- | --- |
| `POST` | `/users/` | Público | Cadastra um usuário com a função `user`. |
| `POST` | `/users/login` | Público | Verifica as credenciais e cria os cookies de autenticação. |
| `POST` | `/refresh` | Refresh token | Gera um novo access token. |
| `POST` | `/users/logout` | Público | Remove os cookies de access e refresh token. |
| `GET` | `/users/` | Administrador | Lista os usuários cadastrados. |
| `GET` | `/users/<id>` | Administrador | Busca um usuário pelo ID. |

## Fluxo de autenticação

1. O usuário envia e-mail e senha para `/users/login`.
2. A senha é comparada com o hash Argon2 armazenado no banco.
3. O backend cria um access token de curta duração e um refresh token válido por sete dias.
4. Os tokens são armazenados em cookies `HttpOnly`.
5. O access token é validado pelo decorador `token_required` nas rotas protegidas.
6. Quando o access token expira, `/refresh` utiliza o refresh token para gerar outro.
7. O logout remove os dois cookies do navegador.

O frontend deve enviar `credentials: "include"` nas requisições que utilizam os cookies.

## Cadastro e permissões

Todo cadastro público recebe obrigatoriamente a função `user`. O cliente não pode escolher a função `admin`.

Para criar um administrador de teste, cadastre o usuário normalmente e altere sua função diretamente no banco:

```sql
UPDATE usuarios
SET role = 'admin'
WHERE email = 'admin@exemplo.com';
```

## Frontend

O frontend está na pasta `front-end/`, na raiz deste repositório. Ele possui páginas simples para cadastro, login e consumo das rotas do backend.

O CORS está configurado para aceitar o frontend executado em `http://127.0.0.1:5500`. As páginas devem ser abertas por um servidor local, como a extensão Live Server do VS Code.

## Segurança aplicada

- Senhas não são armazenadas em texto puro.
- A senha não é incluída nas respostas da API.
- A chave JWT fica em uma variável de ambiente.
- Access e refresh tokens possuem tipos e tempos de expiração diferentes.
- Cookies `HttpOnly` impedem o acesso direto aos tokens por JavaScript.
- Rotas administrativas verificam a função atual do usuário no banco.

## Próximos estudos

- Criar testes automatizados com `pytest`.
- Melhorar a padronização das respostas de erro.
- Estudar proteção contra CSRF em autenticação baseada em cookies.
- Usar cookies `Secure` e HTTPS em produção.
- Estudar rotação e revogação de refresh tokens.

## Observação

Este é um projeto de estudos. A intenção é praticar os conceitos fundamentais de backend e autenticação antes de adicionar arquiteturas ou abstrações mais avançadas.
