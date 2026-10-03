

import logging
from functools import wraps
from flask import g, request

from tokens import verificar_token

logger = logging.getLogger(__name__)


def token_required(funcao):
    
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("access_token")
        if not token:
            logger.warning(
                "Token nao informado metodo=%s rota=%s",
                request.method,
                request.path,
            )
            return {"erro": "Token não informado"}, 401

        payload = verificar_token(token, "access")
        if payload is None:
            logger.warning(
                "Tentativa de acesso com token invalido ou expirado metodo=%s rota=%s",
                request.method,
                request.path,
            )
            return {"Erros": "Token invalido ou expirado"}, 401

        try:
            g.usuario_id = int(payload.get("sub"))
        except (TypeError, ValueError):
            return {"erro": "ID do usuario invalido no token"}, 401

        return funcao(*args, **kwargs)

    return wrapper
