import jwt
from dotenv import load_dotenv
import os

import datetime
from flask import request, g
from models import  Usuario , abrir_session
from Schemas import UsuarioLogin
from pydantic import ValidationError
from sqlalchemy import select
from models import password_hash
from argon2.exceptions import VerifyMismatchError
from functools import wraps

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET não foi definida no ambiente")
#decorator
def token_required(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("access_token")
        if not token:
                return {"erro": "Token não informado"}, 401
        
    
        payload = verificar_token(token, "access")

        if payload is None: 
            return { "Erros": "Token invalido ou expirado"}, 401

        usuario_id = payload.get("sub")
        # esse (g) faz o seguinte meio que tira o usuario_id do escopo, pois antes dele outras functions 
        # nao conseguiam acessar quando usamos o decorator pois so iria existir dentro do wrapper
        g.usuario_id = usuario_id


        return funcao(*args , **kwargs)
    return wrapper



def criar_access_token(usuario_id, tipo="access"):
    data_expiracao= (datetime.datetime.now(datetime.timezone.utc)
                        + datetime.timedelta(minutes=15)
    )
    payload ={"sub": str(usuario_id),
               "exp": data_expiracao, 
               "token_type": tipo
               }
    jwt_codificado = jwt.encode(payload,
                                JWT_SECRET,
                                  algorithm=ALGORITHM)
    return jwt_codificado

def criar_refresh_token(usuario_id, tipo="refresh"):
    data_expiracao= (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
                     )
    payload = { 
        "sub": str(usuario_id),
        "exp": data_expiracao,
        "token_type": tipo
    }
    jwt_codificado = jwt.encode(payload, JWT_SECRET,algorithm=ALGORITHM)
    return jwt_codificado

def verificar_token(token, tipo_esperado="access"):
    try:
        payload = jwt.decode(
                            token,
                            JWT_SECRET,
                            algorithms=[ALGORITHM]
                            )
        tipo = payload.get("token_type")
      

        if tipo != tipo_esperado:
            return None
        
        return payload

    except jwt.ExpiredSignatureError: 
        return None

    except jwt.InvalidTokenError:
        return None


def verificacao_role(role_esperada="admin"):
    usuario_id = g.usuario_id 
    
    with abrir_session() as session:
        usuario = session.get(Usuario, int (usuario_id)) 
        
        if usuario is None:
            return {"erro": "Usuario do token nao existe"}, 401        

        if usuario.role !=role_esperada:
            return {"erro": "Acesso negado"}, 403  
      
    return True



def verificar_login():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return False, None
    
    try:
        user_validado = UsuarioLogin(**dados)
    except ValidationError:
        return False , None

    with abrir_session() as session:
            
        usuario  = session.execute(select(Usuario).where(Usuario.email == user_validado.email)
        ).scalar_one_or_none()

        if not usuario:
            return False, None
    try:
        if not password_hash.verify(usuario.senha,user_validado.senha ):
            return False, None
    except VerifyMismatchError:
        return False , None 

    return True ,usuario
    

