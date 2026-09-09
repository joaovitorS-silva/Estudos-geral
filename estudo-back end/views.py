from flask import render_template ,request
from main import app
from models import  Usuario , abrir_session
from Schemas import UsuarioCreate, UsuarioResponse ,UsuarioListResponse, UsuarioLogin
from pydantic import ValidationError
from sqlalchemy import select
from models import password_hash
from argon2.exceptions import VerifyMismatchError
from dependencias import criar_access_token , verificar_token, criar_refresh_token



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
        access_token = criar_access_token(Usuario.id)
        refresh_token = criar_refresh_token(Usuario.id)
        return{"access_token": access_token,"refresh_token": refresh_token   }
        
    else: 
        return{"error": "email ou senha incorretos"} ,401



@app.route("/listar/usuarios")
def listar_todos():
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
    
    payload = verificar_token(token)
    
    if payload is None:
        return {"msg": "Unauthorized"},401
    
    usuario_id = payload.get("sub")

    print(f"o Usuario de id: {usuario_id} estar fazendo a requisição")
    
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



@app.route("/refresh")
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