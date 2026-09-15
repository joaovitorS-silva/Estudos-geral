import jwt
from dotenv import load_dotenv
import os
import jwt
import datetime
from flask import request
from models import  Usuario , abrir_session
from Schemas import UsuarioLogin
from pydantic import ValidationError
from sqlalchemy import select
from models import password_hash
from argon2.exceptions import VerifyMismatchError


load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")


def criar_access_token(usuario_id, tipo="access"):
    data_expiracao= (datetime.datetime.now(datetime.timezone.utc)
                        + datetime.timedelta(minutes=25)
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


def verificacao_role(role_esperada):
    
    authorization = request.headers.get("Authorization")
    partes = authorization.split()
    token = partes[1]

    payload = verificar_token(token)

    if payload is None :
        return {"msg": "Unauthorized"},401

    usuario_id = payload.get("sub")

     
    with abrir_session() as session:
        user = session.get(Usuario, usuario_id)
    usuario_role = user.role

    if usuario_role  !=role_esperada:
        return {"erro": "Acesso negado"}, 403    
    return True



def verificar_login():
    dados = request.get_json()
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
    

