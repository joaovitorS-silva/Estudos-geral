from flask import render_template ,request
from main import app
from models import  Usuario , abrir_session
from Schemas import UsuarioCreate, UsuarioResponse ,UsuarioListResponse, UsuarioLogin
from pydantic import ValidationError
from sqlalchemy import select
from models import password_hash
from argon2.exceptions import VerifyMismatchError



def verificar_login():
    dados = request.get_json()
    try:
        user_validado = UsuarioLogin(**dados)
    except ValidationError:
        return False

    with abrir_session() as session:
            
        usuario  = session.execute(select(Usuario).where(Usuario.email == user_validado.email)
        ).scalar_one_or_none()

        if not usuario:
            return False
    try:
        if not password_hash.verify(usuario.senha,user_validado.senha ):
            return False
    except VerifyMismatchError:
        return False
    return True





@app.route("/usuarios", methods=["POST"])
def criar_user():
    dados = request.get_json()
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
                admin=usuario_validado.admin
            )

        session.add(novo_user)
        session.commit()
        session.refresh(novo_user)

        usuario_formatado = UsuarioResponse.model_validate(novo_user)
    return usuario_formatado.model_dump(),201





@app.route("/login", methods=["POST"])
def login():
    if verificar_login():
        return {"mensagem":"user fez login com sucesso"}, 200
    else: 
        return{"error": "email ou senha incorretos"} ,401



@app.route("/listar/usuarios")
def listar_todos():

    with abrir_session() as session:
        todos =  session.query(Usuario).all() 
        resposta = UsuarioListResponse(usuarios=todos)
    return  resposta.model_dump(),200






@app.route("/procurar/<int:usr>")
def filtro_user(usr):
    with abrir_session() as session:
        filtro = session.execute(select(Usuario).where(Usuario.id == usr))
        Usuario1 = filtro.scalar_one_or_none()
        if Usuario1 is None:
            return{"Error": "usuario nao encontrado"}, 404
        else:
            user_formatado = UsuarioResponse.model_validate(Usuario1)
        return user_formatado.model_dump(),200