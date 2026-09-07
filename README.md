# Projeto de Autenticação

Monorepo de estudos com frontend e backend separados no mesmo repositório.

## Estrutura

```text
front-end/
  cadastro.html
  login.html
  logado.html
  login.js
  script.js
  style.css

estudo-back end/
  main.py
  models.py
  views.py
  Schemas.py
  alembic/
  requirements.txt
```

## Backend

O backend usa Flask, SQLAlchemy, PostgreSQL, Pydantic, Argon2 e Alembic.

Consulte [estudo-back end/README.md](estudo-back%20end/README.md) para as
instruções de instalação, configuração do banco e rotas da API.

Para iniciar:

```bash
cd "estudo-back end"
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python main.py
```

O backend ficará disponível em `http://127.0.0.1:5000`.

## Frontend

O frontend é composto por páginas HTML, CSS e JavaScript sem dependências de
Node.js. Ele faz requisições para o backend em `http://127.0.0.1:5000`.

Para abrir as páginas, use um servidor estático local, como o Live Server do
VS Code, e acesse `front-end/login.html` ou `front-end/cadastro.html`.

## Próximos passos

- Implementar autenticação com JWT.
- Proteger as rotas que exigem usuário autenticado.
- Adicionar permissões para administradores.
- Criar testes automatizados para backend e frontend.
