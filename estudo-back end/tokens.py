"""Configuração, criação e validação de tokens JWT."""

import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET não foi definida no ambiente")


def _criar_token(usuario_id, tipo, validade):
    payload = {
        "sub": str(usuario_id),
        "exp": datetime.now(timezone.utc) + validade,
        "token_type": tipo,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


def criar_access_token(usuario_id, tipo="access"):
    """Cria um token de acesso com validade de 25 minutos."""
    return _criar_token(usuario_id, tipo, timedelta(minutes=25))


def criar_refresh_token(usuario_id, tipo="refresh"):
    """Cria um token de renovação com validade de sete dias."""
    return _criar_token(usuario_id, tipo, timedelta(days=7))


def verificar_token(token, tipo_esperado="access"):
    """Retorna o payload ou None se o token for inválido, expirado ou de outro tipo."""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        return None

    if payload.get("token_type") != tipo_esperado:
        return None

    return payload
