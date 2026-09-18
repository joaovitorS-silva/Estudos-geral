from flask import render_template ,request, Blueprint

from dependencias import criar_access_token , verificar_token, criar_refresh_token, verificar_login, token_required

auth_users = Blueprint("auth", __name__)

@auth_users.route("/users/login", methods=["POST"])
def login():
    sucesso,usuario = verificar_login()
    if sucesso:
        access_token = criar_access_token(usuario.id) 
        refresh_token = criar_refresh_token(usuario.id)
        return{"access_token": access_token,"refresh_token": refresh_token   } 
        
    else: 
        return{"error": "email ou senha incorretos"} ,401


#@auth_users.route("/refresh")
#def acesso_token_accesss():
    #usuario_id = payload.get("sub")
   # novo_access_token = criar_access_token(usuario_id)

   # return {
    #    "access_token": novo_access_token
    #}, 200