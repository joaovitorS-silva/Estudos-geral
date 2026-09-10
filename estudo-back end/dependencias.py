import jwt
from dotenv import load_dotenv
import os
import jwt
import datetime
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


