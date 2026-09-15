from flask import render_template ,request, Blueprint

from dependencias import criar_access_token , verificar_token, criar_refresh_token, verificar_login

auth_users = Blueprint("auth", __name__)

@auth_users.route("/login", methods=["POST"])
def login():
    sucesso,usuario = verificar_login()
    if sucesso:
        access_token = criar_access_token(usuario.id) 
        refresh_token = criar_refresh_token(usuario.id)
        return{"access_token": access_token,"refresh_token": refresh_token   } 
        
    else: 
        return{"error": "email ou senha incorretos"} ,401


@auth_users.route("/refresh")
def acesso_token_accesss():
    authorization = request.headers.get("Authorization")

    #peguei isso daqui da ia, pois oque este codigo faz é o seguinte valida qualquer coisa que colocar 
    # pois bearer independente dos espaços ou nao, alem de validaro "BEAter""beaARER" e assim vai, odeio FLASK vtnc tudo na mao sapoora
    if not authorization:
        return {"erro": "Token não informado"}, 401

    partes = authorization.split()

    if len(partes) != 2 or partes[0].lower() != "bearer":
        return {"erro": "Formato do token inválido"}, 401

    token = partes[1]
    #cima ^^^^^^^^^

    payload = verificar_token(token, "refresh")

    if payload is None: 
        return { "Erros": "refreh token invalido ou exppirado"}, 401


    usuario_id = payload.get("sub")
    novo_access_token = criar_access_token(usuario_id)

    return {
        "access_token": novo_access_token
    }, 200