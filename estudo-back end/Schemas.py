from pydantic import BaseModel, EmailStr , ConfigDict, Field
from datetime import datetime
from typing import Optional, List 
class UsuarioCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nome: str = Field(min_length=2, max_length=100)
    email: EmailStr
    senha: str = Field(min_length=2, max_length=100)


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



