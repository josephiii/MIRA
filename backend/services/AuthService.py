
import bcrypt
from schemas.AuthSchema import RegisterSchema, LoginSchema

class AuthService:

    def register(self, userData: RegisterSchema):
        
        #TODO check db for existing user
        userExists = None # <-- this should be a lookup that searches for user, if found returns true and user cannot register
        if userExists:
            return "User already exists change email/username"
        
        #TODO add pwd requirements here

        hashedPwd = bcrypt.hashpw(
            userData.password.encode("utf-8"),
            bcrypt.gensalt()
        )

        newUser = {
            "username": userData.username,
            "email": userData.email,
            "password": hashedPwd.decode("utf-8")
        }

        #TODO add newUser to db

        return "User Added" # <-- improve


    def login(self, userData: LoginSchema):
        
        user = None # <-- this should be a look up that pulls the users info from db

        if not user:
            return "Username or pwd incorrect"
        
        validPwd = bcrypt.checkpw(
            userData.password.encode("utf-8"),
            user["password"].encode("utf-8")
        )
        
        if not validPwd:
            return "Username or pwd incorrect"
        
        #TODO return user object with jwt