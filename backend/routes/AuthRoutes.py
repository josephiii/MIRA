
from fastapi import APIRouter
from services.AuthService import AuthService
from schemas.AuthSchema import RegisterSchema, LoginSchema

router = APIRouter()

service = AuthService()

## MAKE SURE TO ADD PROPER ERROR RESPONSES FOR LOGIN AND RESGISTER!!
@router.post("/register")
async def register(userData: RegisterSchema):
    response = service.register(userData)

    if not response:
        return "Error" # <---- HERE
    return response

@router.post("/login")
async def login(userData: LoginSchema):
    
    response = service.login(userData)

    if not response:
        return "Error" # <---- HERE
    return response

