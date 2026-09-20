from flask import  request, Blueprint, make_response

from dependencias import criar_access_token , verificar_token, criar_refresh_token, verificar_login

auth_users = Blueprint("auth", __name__)

@auth_users.route("/users/login", methods=["POST"])
def login():
    sucesso,usuario = verificar_login()
    if sucesso:
        access_token = criar_access_token(usuario.id) 
        refresh_token = criar_refresh_token(usuario.id)

        resposta = make_response({"mensagem": "login concluido"})

        resposta.set_cookie("access_token", access_token, httponly=True)
        resposta.set_cookie("refresh_token", refresh_token, httponly=True)

        return resposta 
        
    else: 
        return{"error": "email ou senha incorretos"} ,401


@auth_users.route("/refresh", methods=["POST"])
def acesso_token_accesss():
    teste = request.cookies.get("refresh_token")
    payload = verificar_token(teste, "refresh")
    if payload is None:
        return({"error": "erro de token INvalido123"}), 401
    usuario_id = payload.get("sub")
    novo_access_token = criar_access_token(usuario_id)
    print(request.cookies)
    resposta = make_response({"mensagem": "access renovado Cuida"})
    resposta.set_cookie("access_token", novo_access_token, httponly=True)
    return resposta , 200


@auth_users.route("/users/logout", methods=["POST"])
def logout():
    resposta = make_response({"mensagem": "logout foi bem sucesido(eu acho)"})

    resposta.delete_cookie("access_token")
    resposta.delete_cookie("refresh_token")

    return resposta






