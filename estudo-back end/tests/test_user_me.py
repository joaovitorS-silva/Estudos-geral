from datetime import timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DateBase import models
from main import app
from tokens import _criar_token, criar_access_token, criar_refresh_token


@pytest.fixture
def client(monkeypatch):
    engine = create_engine("sqlite:///:memory:")
    models.Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    monkeypatch.setattr(models, "Session", session_factory)
    with session_factory() as session:
        session.add_all([
            models.Usuario(id=1, nome="Ana", email="ana@example.com", senha="hash-secreto", role="user"),
            models.Usuario(id=2, nome="Bia", email="bia@example.com", senha="outro-hash", role="admin"),
        ])
        session.commit()
    with app.test_client() as client:
        yield client
    engine.dispose()


@pytest.mark.parametrize("usuario_id,nome,role", [(1, "Ana", "user"), (2, "Bia", "admin")])
def test_retorna_apenas_os_proprios_dados(client, usuario_id, nome, role):
    client.set_cookie("access_token", criar_access_token(usuario_id))

    response = client.get("/user/me?usuario_id=2&id=2")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": usuario_id, "nome": nome, "email": f"{nome.lower()}@example.com", "role": role,
    }


@pytest.mark.parametrize("tipo", ["ausente", "invalido", "expirado", "refresh"])
def test_rejeita_acesso_sem_access_token_valido(client, tipo):
    tokens = {
        "invalido": "token-invalido",
        "expirado": _criar_token(1, "access", timedelta(seconds=-1)),
        "refresh": criar_refresh_token(1),
    }
    if tipo != "ausente":
        client.set_cookie("access_token", tokens[tipo])

    assert client.get("/user/me").status_code == 401


def test_usuario_removido(client):
    client.set_cookie("access_token", criar_access_token(999))

    response = client.get("/user/me")

    assert response.status_code == 404
    assert response.get_json() == {"erro": "usuario nao encontrado"}
