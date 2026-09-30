"""Verificações de credenciais e permissões dos usuários."""

import logging

from argon2.exceptions import VerifyMismatchError
from flask import g, request
from pydantic import ValidationError
from sqlalchemy import select

from DateBase.models import Usuario, abrir_session, password_hash
from DateBase.Schemas import UsuarioLogin

logger = logging.getLogger(__name__)


def verificacao_role(role_esperada="admin"):
    """Verifica a permissão do usuário autenticado por token_required."""
    usuario_id = g.usuario_id

    with abrir_session() as session:
        usuario = session.get(Usuario, int(usuario_id))

        if usuario is None:
            logger.warning("token pertence a usuario inexistente usuario_id=%s", usuario_id)
            return {"erro": "Usuario do token nao existe"}, 401

        if usuario.role != role_esperada:
            logger.warning(
                "Acesso negado usuario_id=%s role=%s role_necessaria=%s",
                usuario.id,
                usuario.role,
                role_esperada,
            )
            return {"erro": "Acesso negado"}, 403

    return True


def verificar_login():
    """Valida as credenciais da requisição e retorna (sucesso, usuario)."""
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return False, None

    try:
        user_validado = UsuarioLogin(**dados)
    except ValidationError:
        return False, None

    with abrir_session() as session:

        usuario = session.execute(
            select(Usuario).where(Usuario.email == user_validado.email)
        ).scalar_one_or_none()

        if not usuario:
            return False, None
    try:
        if not password_hash.verify(usuario.senha, user_validado.senha):
            return False, None
    except VerifyMismatchError:
        return False, None

    return True, usuario
