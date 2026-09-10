from pydantic import BaseModel, EmailStr , ConfigDict
from datetime import datetime
from typing import Optional, List 
class UsuarioCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nome: str
    email: str
    senha: str
    role: str 


class UsuarioLogin(BaseModel):
    email: str
    senha: str
    
class UsuarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str 
    email: str
    role: str 



class UsuarioListResponse(BaseModel):
    usuarios: List[UsuarioResponse] 



