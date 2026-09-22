import pytest
from pydantic import ValidationError
from Schemas import UsuarioCreate

def test_rejeitar_email_invalido():
    with pytest.raises(ValidationError):
        UsuarioCreate(
            nome="João",
            email="email-invlaido",
            senha="123",
        )
def test_criar_usuario_valido():
    usuario =  UsuarioCreate(
                nome="João",
                email="joaovitu968@gmail.com",
                senha="maepai123@34",
            )
    assert usuario.nome == "João"
    assert usuario.email == "joaovitu968@gmail.com"
    assert usuario.senha == "maepai123@34"

def test_rejeitar_senha_curta():
    with pytest.raises(ValidationError):
        UsuarioCreate(
                    nome="João",
                    email="joaovitu968@gmail.com",
                    senha="12",
                )

def test_rejeitar_nome_curto():
    with pytest.raises(ValidationError):
         UsuarioCreate(
                    nome="J",
                    email="joaovitu968@gmail.com",
                    senha="maepai123@34",
                )