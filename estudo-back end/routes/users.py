from flask import render_template ,request, Blueprint
from models import  Usuario , abrir_session
from Schemas import UsuarioCreate, UsuarioResponse ,UsuarioListResponse, UsuarioLogin
from pydantic import ValidationError
from sqlalchemy import select
from models import password_hash
from dependencias import  verificar_token , verificacao_role, token_required
from flask import g

users = Blueprint("/users", __name__ )

@users.route("/users/", methods=["POST"])
def criar_user():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return {"erro": "JSON invalido ou nao informado"}, 400
    try:
        usuario_validado = UsuarioCreate(**dados)
    except ValidationError as erro:
        return {"erro ": erro.errors()}, 400

    with abrir_session() as session:
        usuario = session.execute(select(Usuario).where(Usuario.email == usuario_validado.email)
 ).scalar_one_or_none()
        if usuario is not None:
            return {"Erro": "Usuario ja cadastrado"}, 409
    
        senha_criptografada = password_hash.hash(usuario_validado.senha)
        novo_user = Usuario(
                nome=usuario_validado.nome,
                email=usuario_validado.email,
                senha=senha_criptografada,
                role="user"
            )

        session.add(novo_user)
        session.commit()
        session.refresh(novo_user)

        usuario_formatado = UsuarioResponse.model_validate(novo_user)
    return usuario_formatado.model_dump(),201




@users.route("/users/", methods=["GET"])
@token_required
def listar_todos():

    resultado = verificacao_role()
    if resultado is not True:
        return resultado
    
    with abrir_session() as session:
        todos =  session.query(Usuario).all()

        resposta = UsuarioListResponse(usuarios=todos)

    return  resposta.model_dump(),200 , 



@users.route("/users/<int:usr>" , methods=["GET"])
@token_required
def filtro_user(usr):
    resultado = verificacao_role()
    if resultado is not True:
        return resultado
    with abrir_session() as session:
        filtro = session.execute(select(Usuario).where(Usuario.id == usr))
        Usuario1 = filtro.scalar_one_or_none()
        if Usuario1 is None:
            return{"Error": "usuario nao encontrado"}, 404  
        else:
            user_formatado = UsuarioResponse.model_validate(Usuario1)
        return user_formatado.model_dump(),200



